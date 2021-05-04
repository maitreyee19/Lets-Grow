from .. import db

class Post(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'posts'
    
    uuid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.uuid'))

    def __repr__(self):
        return '<Post %r>' % self.title