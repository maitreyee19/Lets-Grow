import uuid
from datetime import datetime

from main import db
from main.model import User
from main.model.post import Post


def save_new_post(data):
    # post = Post.query.filter_by(title=data['title'], author_id=data['author_id']).first()
    # if not post:
    new_post = Post(
        title=data['title'],
        body=data['body'],
        author_id=data['author_id'],
        postLatitude =data['postLatitude'],
        postLongitude = data['postLongitude'],
        userLatitude = data ['userLatitude'],
        userLongitude =data['userLongitude'],
        topic_id =data['topic_id'],
        subtopics_id =data['subtopics_id'],
        age_group = data['age_group'],
        establishmentInfo =data['establishmentInfo'],
        establishmentType =data['establishmentType'],


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
    # post_data = Post.query.all()
    post_data = db.session.query(Post, User).outerjoin(User, Post.author_id == User.uuid).all()
    print(post_data)
    return post_data


def get_a_post(title):
    return Post.query.filter_by(title=title).first()



def save_changes(data):
    db.session.add(data)
    db.session.commit()
