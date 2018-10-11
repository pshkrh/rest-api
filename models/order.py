from db import db

class OrderModel(db.Model):

    __tablename__ = 'orders'

    order_no = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(80))
    name = db.Column(db.String(80))
    quantity = db.Column(db.String(80))
    price = db.Column(db.String(80))
    delivery_date = db.Column(db.String(80))
    currency = db.Column(db.String(80))

    def __init__(self,order_no,product_code,name,quantity,price,delivery_date,currency):
        self.order_no = order_no
        self.product_code = product_code
        self.name = name
        self.quantity = quantity
        self.price = price
        self.delivery_date = delivery_date
        self.currency = currency

    def json(self):
        return {'order_no': self.order_no, 'product_code': self.product_code, 'name': self.name, 'quantity': self.quantity, 'price': self.price,'delivery_date': self.delivery_date, 'currency': self.currency}   

    @classmethod
    def find_by_order_no(cls,order_no):
        return cls.query.filter_by(order_no = order_no).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    