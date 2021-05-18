from flask import request
from flask_restplus import Resource

from ..service.dto import TopicsDto
from ..service.topics_service import get_all_topics,get_a_topic

api = TopicsDto.topics_api
_topics = TopicsDto.topics


@api.route('/')
class TopicsList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_topics, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_topics()

