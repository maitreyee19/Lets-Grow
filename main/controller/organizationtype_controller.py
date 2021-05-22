from flask import request
from flask_restplus import Resource

from ..service.dto import OrganizationType
from ..service.organizationtype_service import get_all_typeOfOrg, get_one_typeofOrg

api = OrganizationType.org_api
_orgType = OrganizationType.orgType


@api.route('/')
class OrgList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_orgType, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_typeOfOrg()
