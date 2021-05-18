from .. import db


class TypeOfOrganization(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'organizationType'

    uuid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))


    def __repr__(self):
        return '<Post %r>' % self.title
