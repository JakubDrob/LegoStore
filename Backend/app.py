from flask import Flask
from flask_restful import Api
from resources.user_resource import User
from resources.product_resource import Product
from resources.set_resource import Set
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(User, '/users', '/users/<string:user_id>')
api.add_resource(Product, '/products')
api.add_resource(Set, '/sets')

if __name__ == "__main__":
    app.run(debug=True)
