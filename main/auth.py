# Third-party libraries
from flask import Flask, redirect, request, url_for ,Blueprint, g , render_template, session
import functools
# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
import os
from .service.user_service import get_a_user


basedir = os.path.abspath(os.path.dirname("manage.py"))
bp = Blueprint('auth', __name__, url_prefix='/auth')

def get_config():
    with open( os.path.join(basedir, 'google-oidc.json'), 'r') as config_file:
        config_data = json.load(config_file)
        return config_data

def get_google_provider_cfg():
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()


config = get_config()

# OAuth 2 client setup
client = WebApplicationClient(config["client_id"])
    # "1032839014332-44tte7j9ndhgl4hqtjaojhcq5sst6rse.apps.googleusercontent.com")

def user_validation(emailAddress):
    user = get_a_user(emailAddress)
    if user is None:

        return False
    else:
        return user






@bp.route("/login")
def login():

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri("https://accounts.google.com/o/oauth2/auth",
                                                redirect_uri=request.url_root + "auth/callback",
                                                scope=[
                                                    "openid", "email", "profile"],
                                                )
    return redirect(request_uri)

@bp.route("/callback")
def callback():
    import os
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
        auth=(config["client_id"] , config["client_secret"])
        # "1032839014332-44tte7j9ndhgl4hqtjaojhcq5sst6rse.apps.googleusercontent.com","dMl6H-26baE8LRjmi71S7dGv"),
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
        user.setUserLink(picture)
        if  user is not None:
            print("user exists")
            print(user.userImageLink)

        else:
            print("register user")

    else:
        return( "User email not available or not verified by Google.", 400 )
    print("unique_id {} users_email {} picture {} users_name {} ".format(
        unique_id, users_email, picture, users_name))
    return ("welcom {}".format(users_name) , 200)

