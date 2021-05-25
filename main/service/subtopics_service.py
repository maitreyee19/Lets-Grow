import uuid
import datetime

from main import db
from main.model.subtopics import Subtopics
from main.model.topics import Topics


def get_all_subtopics():
    return Subtopics.query.all()


def get_subtopics_of_parentTopic(parent_topics_name):
    topic = Topics.query.filter_by(topics_name=parent_topics_name).first()
    print("topics details:",topic.uuid)
    return Subtopics.query.filter_by(parent_topics_id=topic.uuid).all()
