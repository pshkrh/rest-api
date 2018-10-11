from flask import Flask
from flask_restful import Resource, Api
from resources.order import Order, OrderList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)

api.add_resource(Order, '/order/<string:order_no>')
api.add_resource(OrderList, '/orders')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True