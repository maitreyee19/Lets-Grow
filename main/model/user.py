from .. import db
from flask_login import UserMixin

class User(db.Model ,UserMixin):

    """ User Model for storing user related details """
    __tablename__ = 'users'


    uuid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    lastLogin = db.Column(db.Date)
    registeredUser = db.Column(db.Boolean, default=False)
    userImageLink = db.Column(db.String(256))

    # def __init__(self):
        # self.userImageLink = None

    # posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.username

    def setUserLink(self,imagePath):
        self.userImageLink = imagePath
    
    def setID(self,id):
        self.id = id
