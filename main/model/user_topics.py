from .. import db


class User_topics(db.Model):
    """ User Model for storing user related details """
    __tablename__ = 'users_topics'

    userId = db.Column(db.Integer, db.ForeignKey('users.uuid'), primary_key=True)
    topicsId = db.Column(db.Integer, db.ForeignKey('sub_topics.uuid'), primary_key=True)

    # posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.username
