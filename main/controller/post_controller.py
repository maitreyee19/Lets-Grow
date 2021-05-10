from flask import request
from flask_restplus import Resource

from ..service.dto import PostDto
from ..service.post_service import get_all_posts, save_new_post, get_a_post
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = PostDto.api
_post = PostDto.post


@api.route('/')
class PostList(Resource):
    @api.doc('list_of_all_posts')
    @api.marshal_list_with(_post, envelope='data')
    def get(self):
        """List all registered posts"""
        return get_all_posts()

    @api.response(201, 'post is successful.')
    @api.doc('create a new post')
    @api.expect(_post, validate=True)
    def post(self):
        """Creates a new post """
        data = request.json
        return save_new_post(data=data)


@api.route('/post')
@api.param('title', 'The post identifier')
@api.response(404, 'post not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_post)
    def get(self, title):
        """get a post given its title"""
        post = get_a_post(title)
        if not post:
            api.abort(404)
        else:
            return post
