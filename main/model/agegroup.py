from .. import db


class AgeGroup(db.Model):
    """ User Model for different categories of posts """
    __tablename__ = 'age_category'

    uuid = db.Column(db.Integer, primary_key=True)
    age_category = db.Column(db.String(256), index=True)

    def __repr__(self):
        return '<Post %r>' % self.age_category
