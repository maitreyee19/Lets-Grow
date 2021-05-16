import uuid
import datetime

from main import db
from main.model.topics import Topics


def get_all_topics():
    return Topics.query.all()


def get_a_topic(subject):
    return Topics.query.filter_by(topics_name=subject).first()
