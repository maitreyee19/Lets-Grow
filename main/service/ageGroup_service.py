import uuid
import datetime

from main import db
from main.model.agegroup import AgeGroup


def get_all_ageGroup():
    return AgeGroup.query.all()


def get_a_ageGroup(age_category):
    return AgeGroup.query.filter_by(age_category=age_category).first()
