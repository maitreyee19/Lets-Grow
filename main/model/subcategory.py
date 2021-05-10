from .. import db


class Subcategory(db.Model):
    """ User Model for storing Posts related details """
    __tablename__ = 'posts'

    uuid = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.uuid'))
    subcategory_name = db.Column(db.String(256), index=True)




    def __repr__(self):
        return '<Post %r>' % self.title
