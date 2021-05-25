from flask import request
from flask_restplus import Resource

from ..service.dto import TopicsDto
from ..service.dto import SubTopicsDto
from ..service.topics_service import get_all_topics
from ..service.subtopics_service import get_subtopics_of_parentTopic

api = TopicsDto.topics_api
_topics = TopicsDto.topics
_subTopics = SubTopicsDto.subtopics


@api.route('/')
class TopicsList(Resource):
    @api.doc('list_of_ageGroup')
    @api.marshal_list_with(_topics, envelope='data')
    def get(self):
        """List all listed Topics"""
        return get_all_topics()


@api.route('/<topicname>')
@api.param('topicname', 'The  identifier')
@api.response(404, 'topic not found.')
class Topic(Resource):
    @api.doc('get sub topics')
    @api.marshal_with(_subTopics)
    def get(self, topicname):
        """get a topic its identifier"""
        print("get subtopic of parent topic:",topicname)
        subTopics = get_subtopics_of_parentTopic(topicname)
        if not subTopics:
            api.abort(404)
        else:
            return subTopics
