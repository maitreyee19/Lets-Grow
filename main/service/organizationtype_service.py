import uuid
import datetime

from main import db
from main.model.organization_type import TypeOfOrganization


def get_all_typeOfOrg():
    return TypeOfOrganization.query.all()


def get_one_typeofOrg(name):
    return TypeOfOrganization.query.filter_by(name=name).first()
