from flask import request
from flask_restplus import Resource

from ..service.dto import AgeGroupDto
from ..service.ageGroup_service import get_all_ageGroup,get_a_ageGroup

api = AgeGroupDto.ageGroup_api
_agegroup = AgeGroupDto.ageGroup


@api.route('/')
class AgeGroupList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_agegroup, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_ageGroup()

