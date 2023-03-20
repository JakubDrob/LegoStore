from flask_restful import Resource
from database import get_sets


class Set(Resource):
    def get(self):
        sets = get_sets()
        return {'sets': sets}, 200
