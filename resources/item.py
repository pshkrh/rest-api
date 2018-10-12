from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('quantity')
    parser.add_argument('price')
    parser.add_argument('delivery_date')
    parser.add_argument('currency')
    parser.add_argument('order_no')

    def get(self, product_code):
        item = ItemModel.find_by_product_code(product_code)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404    

    def post(self,product_code):
        if ItemModel.find_by_product_code(product_code):
            return {'message': "An Item with product code '{}' already exists.".format(product_code)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(product_code, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured while inserting this item.'}, 500

        return item.json(), 201    

    def delete(self, product_code):
        item = ItemModel.find_by_product_code(product_code)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404    

    def put(self, product_code):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_product_code(product_code)

        if item:
            item.name = data['name']
            item.quantity = data['quantity']
            item.price = data['price']
            item.delivery_date = data['delivery_date']
            item.currency = data['currency']
            item.order_no = data['order_no']
        else:
            item = ItemModel(product_code, **data)

        item.save_to_db()

        return item.json()
        

class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
