from flask import Flask , request
try:
    from flask_restplus import Resource, Api
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, Api
# from flask_bcrypt import Bcrypt
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView
from flask_login import LoginManager

from .config import config_by_name
from .db_connect import db
from .controller.user_controller import api as user_ns
from .controller.post_controller import api as post_ns
from .controller.agegroup_controller import api as agegroup_ns
from .controller.topics_controller import api as topics_ns
from .controller.establishment_controller import api as place_ns
from .controller.organizationtype_controller import api as placetype_ns
from .controller.subtopics_controller import api as subtopics_ns
from .service.dto import UserDto
from .schema import schema
from .auth import auth
from .dashboard import dashBoard

# flask_bcrypt = Bcrypt()
api = Api(
    title='Lets Grow',
    version='1.0',
    description='API For Lets Grow',
)

def create_app(config_name='int'):
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    api.init_app(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    # flask_bcrypt.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(dashBoard)
    api.add_namespace(user_ns, path='/user')
    api.add_namespace(post_ns, path='/post')
    api.add_namespace(agegroup_ns, path='/age_group')
    api.add_namespace(topics_ns, path='/topics')
    api.add_namespace(place_ns, path='/places')
    api.add_namespace(placetype_ns, path='/typeofplace')
    api.add_namespace(subtopics_ns, path='/subtopics')

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.route('/')
    def index():
        return '<p> Hello World!</p>'

    #DONT DO THIS . REMOVE AFTER DEV SERVER 
    # if(config_name == 'dev'):
    @app.after_request
    def after_request(response):
        whiteList = [ "https://bhabanidas.com" , "https://beta.kiribul.com" , "https://kiribul.com" , "https://api.kiribul.com"]
        if request.referrer is not None :
            r = request.referrer[:-1]
            if r in whiteList:
                response.headers.add('Access-Control-Allow-Origin', r)
                response.headers.add("Access-Control-Allow-Credentials" , "true")
                response.headers.add("Access-Control-Allow-Headers", "*")
                response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    @login_manager.user_loader
    def load_user(uuid):
        from .model.user import User
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(uuid)
        
    return app
