from .. import db


class Subtopics(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'sub_topics'

    uuid = db.Column(db.Integer, primary_key=True)
    parent_topics_id = db.Column(db.Integer, db.ForeignKey('topics.uuid'))
    #parent_topics_name = db.Column(db.String(256), db.ForeignKey('topics.topics_name'))

    subtopics_name = db.Column(db.String(256), index=True)




    def __repr__(self):
        return '<Post %r>' % self.subtopics_name
