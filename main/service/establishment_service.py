import uuid
import datetime

from main import db
from main.model.establishmentInfo import Establishment
from main.model.organization_type import TypeOfOrganization


def get_all_places():
    return Establishment.query.all()


def get_a_placeByName(name):
    return Establishment.query.filter_by(name=name).first()


def get_a_placeByType(name):
    pass
