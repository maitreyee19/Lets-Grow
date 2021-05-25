# Third-party libraries
from main.model.user import User
import os
from flask import Flask, redirect, request, url_for, Blueprint, g, render_template, session
from flask_restplus import Api , fields
# import functools
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    #     logout_user,
)
from flask_restplus import Resource
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
from main.service.user_service import get_a_user
from main import db
# from main import UserDto


basedir = os.path.abspath(os.path.dirname("manage.py"))
auth = Blueprint('auth', __name__, url_prefix='/auth')

api = Api(auth, title='lets grow auth',
          version='1.0',
          description='A description',)


def get_config():
    with open(os.path.join(basedir, 'google-oidc.json'), 'r') as config_file:
        config_data = json.load(config_file)
        return config_data


def get_google_provider_cfg():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()


config = get_config()

# OAuth 2 client setup
client = WebApplicationClient(config["client_id"])


@auth.route("/login")
def login():
    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri("https://accounts.google.com/o/oauth2/auth",
                                             redirect_uri=request.url_root + "auth/callback",
                                             scope=["openid", "email", "profile"], )
    return redirect(request_uri)


@auth.route("/callback")
def callback():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        "https://oauth2.googleapis.com/token",
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(config["client_id"], config["client_secret"])
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    google_provider_cfg = get_google_provider_cfg()
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        user = get_a_user(users_email)
        print(user)
        if user is not None:
            user.setID(user.uuid)
            user.setUserLink(picture)
            login_user(user)
            print("current_user",current_user)
            # session["user"] = users_email
            return redirect("http://letsgrow.com:3000/")
        else:

            session["useremail"] = users_email
            new_user = User(
                email=users_email,
                username=users_name,
                registeredUser=False
            )
            new_user.setID(new_user.uuid)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            print(current_user)
            return redirect("http://letsgrow.com:3000/#/register?users_email="+users_email)

    else:
        return ("User email not available or not verified by Google.", 400)


UserDto = api.model('user', {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'userImageLink': fields.String(required=True, description='user image')
})



@api.route('/register')
class Register(Resource):
    @api.doc('Get current user Details')
    @api.marshal_list_with(UserDto, envelope='data')
    def post(self):
        try:
            user = current_user
            print(current_user.name)
        except:
            print("no logged in user")
        return user


@api.route('/userDetail')
class CurrentUser(Resource):
    @api.doc('Get current user Details')
    @api.marshal_list_with(UserDto, envelope='data')
    def get(self):
        try:
            user = current_user
            print(current_user.name)
        except:
            print("no logged in user")
        return user
