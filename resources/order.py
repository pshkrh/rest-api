from flask_restful import Resource, reqparse
from models.order import OrderModel


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('product_code')
    parser.add_argument('name')
    parser.add_argument('quantity')
    parser.add_argument('price')
    parser.add_argument('delivery_date')
    parser.add_argument('currency')

    def get(self, order_no):
        order = OrderModel.find_by_order_no(order_no)
        if order:
            return order.json()
        return {'message': 'Order not found'}, 404    

    def post(self, order_no):
        if OrderModel.find_by_order_no(order_no):
            return {'message': "An Order with order number '{}' already exists.".format(order_no)}, 400

        data = Order.parser.parse_args()
        print(data)

        order = OrderModel(order_no, data['product_code'], data['name'], data['quantity'], data['price'], data['delivery_date'], data['currency'])
        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting this order.'}, 500

        return order.json(), 201    

    def delete(self, order_no):
        order = OrderModel.find_by_order_no(order_no)
        if order:
            order.delete_from_db()
            return {'message': 'Order deleted.'}
        return {'message': 'Order not found.'}, 404    

    def put(self, order_no):
        data = Order.parser.parse_args()

        order = OrderModel.find_by_order_no(order_no)

        if order:
            order.product_code = data['product_code']
            order.name = data['name']
            order.quantity = data['quantity']
            order.price = data['price']
            order.delivery_date = data['delivery_date']
            order.currency = data['currency']
        else:
            order = OrderModel(order_no, **data)

        order.save_to_db()

        return order.json()
        

class OrderList(Resource):
    def get(self):
        return {'orders': [order.json() for order in OrderModel.query.all()]}
