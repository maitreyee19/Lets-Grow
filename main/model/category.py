from .. import db


class Categories(db.Model):
    """ User Model for different categories of posts """
    __tablename__ = 'categories'

    uuid = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(256), index=True)

    def __repr__(self):
        return '<Post %r>' % self.title
