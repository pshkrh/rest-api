from flask_restful import Resource
from models.order import OrderModel


class Order(Resource):
    def get(self, order_no):
        order = OrderModel.find_by_order_no(order_no)
        if order:
            return order.json()
        return {'message': 'Order not found'}, 404

    def post(self, order_no):
        if OrderModel.find_by_order_no(order_no):
            return {'message': "A order with order number '{}' already exists.".format(order_no)}, 400

        order = OrderModel(order_no)
        try:
            order.save_to_db()
        except:
            return {"message": "An error occurred creating the order."}, 500

        return order.json(), 201

    def delete(self, order_no):
        order = OrderModel.find_by_order_no(order_no)
        if order:
            order.delete_from_db()

        return {'message': 'Order deleted'}


class OrderList(Resource):
    def get(self):
        return {'orders': [order.json() for order in OrderModel.query.all()]}