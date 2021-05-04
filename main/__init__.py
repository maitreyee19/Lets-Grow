from flask import Flask
try:
    from flask_restplus import Resource, Api
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView
from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
api = Api(
    title='Lets Grow',
    version='1.0',
    description='API For Lets Grow',
    # All API metadatas
)

def create_app(config_name):
    app = Flask(__name__)
    api.init_app(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    @app.route('/')
    def index():
        return '<p> Hello World!</p>'

    from .controller.user_controller import api as user_ns
    api.add_namespace(user_ns, path='/user')
        
    from .schema import schema
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )

    return app
