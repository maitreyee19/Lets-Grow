from flask import request
from flask_restplus import Resource

from ..service.dto import EstablishmentDto
from ..service.establishment_service import get_a_placeByName, get_type_of_org, get_all_places

api = EstablishmentDto.api
_places = EstablishmentDto.establishment


@api.route('/')
class EstablishmentList(Resource):
    @api.doc('list_of_Establishment')
    @api.marshal_list_with(_places, envelope='data')
    def get(self):
        """List all registered subtopics"""
        return get_all_places()

    def getPlaceTypeList(self, name):
        """List all registered subtopics of a topic"""
        return get_type_of_org(name)


@api.route('/<placeInfo>')
@api.param('email', 'The User identifier')
@api.response(404, 'User not found.')
class Place(Resource):
    @api.doc('get place type')
    @api.marshal_with(_places)
    def get(self, placeName):
        """get a user given its identifier"""
        placeType = get_type_of_org(placeName)
        if not placeType:
            api.abort(404)
        else:
            return placeType
