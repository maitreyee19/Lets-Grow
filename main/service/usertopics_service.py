import uuid
import datetime

from main import db
from main.model.user_topics import User_topics


def get_all_topics(userId):
    return User_topics.query.filter_by(userId=userId).first()


def get_all_users(topic_Id):
    return User_topics.query.filter_by(topicsId=topic_Id).first()