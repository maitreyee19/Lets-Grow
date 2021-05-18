from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username')

    })


class PostDto:
    api = Namespace('post', description='user  post related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username')
    })
    post = api.model('post', {
        'title': fields.String(required=True, description='title of the post'),
        'body': fields.String(required=True, description='details about the post'),
        'author_id': fields.Integer(required=True, description='author user id')
        # 'postDate': fields.Date(required=True, description='post date Information')
    })
    post_user = api.model('post_user', {
        'title': fields.String(attribute="Post.title", required=True, description='title of the post'),
        'body': fields.String(attribute="Post.body", required=True, description='details about the post'),
        "User": fields.Nested(user)
        # 'author_id': fields.Integer(required=True, description='author user id')
        # 'postDate': fields.Date(required=True, description='post date Information')
    })


class TopicsDto:
    topics_api = Namespace('topics', description='different categories of userpost')
    topics = topics_api.model('topics', {
        'topics_name': fields.String(required=True, description='title of the category')
    })


class SubTopicsDto:
    subtopics_api = Namespace('subtopics', description='info about subcategory belongs to which category')
    subtopics = subtopics_api.model('subtopics', {
        'parent_topics_id': fields.Integer(required=True, description='parent id'),
        'parent_topics_name':fields.String(required=True, description='parent topic name')


    })


class AgeGroupDto:
    ageGroup_api = Namespace('ageGroup', description='different ageGroup info')
    ageGroup = ageGroup_api.model('ageGroup', {
        'age_category': fields.String(required=True, description='age group details')
    })


class EstablishmentDto:
    api = Namespace('post', description='user  post related operations')
    establishment = api.model('establishment', {
        'name': fields.String(required=True, description='establishment name'),
        'type': fields.String(required=True, description='establishment type'),

        'address': fields.Integer(required=True, description='address info'),
        'placeLongitude': fields.Float(description='geo location'),
        'placeLatitude': fields.Float(description='geo location'),
        'websiteInfo': fields.String(description='establishment web Address')

        # 'postDate': fields.Date(required=True, description='post date Information')
    })


class FavoritesDto:
    api = Namespace('favorites', description='user  favorite post')
    favorites = api.model('favorites', {
        'follower_id': fields.Integer(required=True, description='follower info'),
        'post_id': fields.Integer(required=True, description='follower postId')

        # 'postDate': fields.Date(required=True, description='post date Information')
    })


class UserTopicsDto:
    api = Namespace('userTopics', description='topics user follow')
    favorites = api.model('userTopics', {
        'userId': fields.String(required=True, description='user Id'),
        'topicsId': fields.String(required=True, description='subtopics Id')

    })
