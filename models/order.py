from db import db

class OrderModel(db.Model):

    __tablename__ = 'orders'

    order_no = db.Column(db.Integer, primary_key=True)
    items = db.relationship('ItemModel', lazy='dynamic')
    

    def __init__(self,order_no):
        self.order_no = order_no

    def json(self):
        return {'order_no': self.order_no, 'items': [item.json() for item in self.items.all()]}   

    @classmethod
    def find_by_order_no(cls,order_no):
        return cls.query.filter_by(order_no = order_no).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    