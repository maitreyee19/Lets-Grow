import uuid
import datetime

from main import db
from main.model.establishmentInfo import Establishment
from main.model.organization_type import TypeOfOrganization


def get_all_places():
    return Establishment.query.all()


def get_a_placeByName(name):
    return Establishment.query.filter_by(name=name).first()


def get_type_of_org(name):
    org = Establishment.query.filter_by(name=name).first()
    print("org:",org)
    TypeOfOrganization.query.filter_by(uuid=org.type).first()
