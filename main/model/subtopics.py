from .. import db


class Subtopics(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'sub_topics'

    uuid = db.Column(db.Integer, primary_key=True)
    topics_id = db.Column(db.Integer, db.ForeignKey('topics.uuid'))
    subtopics_name = db.Column(db.String(256), index=True)




    def __repr__(self):
        return '<Post %r>' % self.title
