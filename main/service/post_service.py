import uuid
from datetime import datetime

from main import db
from main.model.post import Post


def save_new_post(data):
    #post = Post.query.filter_by(title=data['title'], author_id=data['author_id']).first()
    #if not post:
    new_post = Post(
        title=data['title'],
        body=data['body'],
        author_id=data['author_id'],
        post_date=datetime.now().date()


        )
    save_changes(new_post)
    response_object = {
        'status': 'success',
        'message': 'Successfully posted a post.'
    }
    return response_object, 201
    # else:
    #     response_object = {
    #         'status': 'fail',
    #         'message': 'unable to post your message.please try again',
    #     }
    #     return response_object, 409


def get_all_posts():
    return Post.query.all()


def get_a_post(title):
    return Post.query.filter_by(title=title).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
