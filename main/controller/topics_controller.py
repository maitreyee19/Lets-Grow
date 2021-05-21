from flask import request
from flask_restplus import Resource

from ..service.dto import TopicsDto
from ..service.topics_service import get_all_topics, get_a_topic
from ..service.subtopics_service import get_subtopics_of_parentTopic

api = TopicsDto.topics_api
_topics = TopicsDto.topics


@api.route('/')
class TopicsList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_topics, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_topics()


@api.route('/<topicName>')
@api.param('topicName', 'The  identifier')
@api.response(404, 'User not found.')
class Topic(Resource):
    @api.doc('get a user')
    @api.marshal_with(_topics)
    def get(self, name):
        """get a user given its identifier"""
        subTopics = get_subtopics_of_parentTopic(name)
        if not subTopics:
            api.abort(404)
        else:
            return subTopics