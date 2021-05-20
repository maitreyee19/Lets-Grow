from .. import db


class Establishment(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'establishment_Info'

    uuid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    type = db.Column(db.Integer, db.ForeignKey('organizationType.uuid'))

    address = db.Column(db.String(256))
    placeLongitude = db.Column(db.Float(10, 9))
    placeLatitude = db.Column(db.Float(10, 9))
    websiteInfo = db.Column(db.String(256))

    def __repr__(self):
        return '<Post %r>' % self.name
