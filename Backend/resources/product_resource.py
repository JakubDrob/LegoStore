from flask_restful import Resource
from database import get_products


class Product(Resource):
    def get(self):
        products = get_products()
        return {'products': products}, 200
