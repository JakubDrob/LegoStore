from flask import Flask
from flask_restful import Api
from resources.user_resource import User
from resources.product_resource import Product
from resources.set_resource import Set

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users', '/users/<string:user_id>')
api.add_resource(Product, '/products')
api.add_resource(Set, '/sets')

if __name__ == "__main__":
    app.run(debug=True)
