import uuid
import datetime

from main import db
from main.model.subtopics import Subtopics


def get_all_subtopics():
    return Subtopics.query.all()


def get_a_subtopic(subject):
    return Subtopics.query.filter_by(subtopics_name=subject).first()
