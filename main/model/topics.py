from .. import db


class Topics(db.Model):
    """ User Model for different topics """
    __tablename__ = 'topics'

    uuid = db.Column(db.Integer, primary_key=True)
    topics_name = db.Column(db.String(256),index=True)

    def __repr__(self):
        return '<Post %r>' % self.topics_name
