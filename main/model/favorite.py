from .. import db


class Favorites(db.Model):
    """  Model for storing  favorite Posts of users """
    __tablename__ = 'favorites'

    follower_id = db.Column(db.Integer, db.ForeignKey('users.uuid'),primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.uuid'),primary_key=True)
    creationDate = db.Column(db.Date)

    def __repr__(self):
        return '<Post %r>' % self.follower_id
