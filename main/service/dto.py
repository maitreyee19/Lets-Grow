from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username')
    })


class PostDto:
    api = Namespace('post', description='user  post related operations')
    post = api.model('post', {
        'title': fields.String(required=True, description='title of the post'),
        'body': fields.String(required=True, description='details about the post'),

        'author_id': fields.Integer(required=True, description='author user id')
        #'postDate': fields.Date(required=True, description='post date Information')
    })
