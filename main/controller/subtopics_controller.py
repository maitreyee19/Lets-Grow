from flask import request
from flask_restplus import Resource

from ..service.dto import SubTopicsDto
from ..service.subtopics_service import get_subtopics_of_parentTopic, get_all_subtopics

api = SubTopicsDto.subtopics_api
_subtopics = SubTopicsDto.subtopics


@api.route('/')
class TopicsList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_subtopics, envelope='data')
    def get(self):
        """List all registered subtopics"""
        return get_all_subtopics()

    def getSubtopicsList(self, parentTopicName):
        """List all registered subtopics of a topic"""
        return get_all_subtopics(parentTopicName)
