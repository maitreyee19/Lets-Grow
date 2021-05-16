import uuid
import datetime

from main import db
from main.model.establishmentInfo import Establishment


def get_all_places():
    return Establishment.query.all()


def get_a_placeByName(name):
    return Establishment.query.filter_by(name=name).first()


def get_a_placeByType(name):
    return Establishment.query.filter_by(type=name).first()
