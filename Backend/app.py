from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

usersList = {
    '1': {'username': 'Piotr', 'password': 'Dupa'},
    '2': {'username': 'Mark', 'password': 'Cat'},
    '3': {'username': 'Brad', 'password': 'Pitt'}
}

class User(Resource):
    def get(self, user_id):
        if user_id in usersList:
            return {'user': usersList[user_id]}, 200
        else:
            return {'message': 'User not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username is required', required=True)
        parser.add_argument('password', type=str, help='Password is required', required=True)
        args = parser.parse_args()
        user_id = str(len(usersList) + 1)
        usersList[user_id] = {
            'username': args['username'],
            'password': args['password']
        }
        return {'message': 'User created', 'user_id': user_id}, 201

    def put(self, user_id):
        if user_id in usersList:
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username is required', required=True)
            parser.add_argument('password', type=str, help='Password is required', required=True)
            args = parser.parse_args()
            usersList[user_id] = {
                'username': args['username'],
                'password': args['password']
            }
            return {'message': 'User updated', 'user_id': user_id}, 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        if user_id in usersList:
            del usersList[user_id]
            return {'message': 'User deleted'}, 200
        else:
            return {'message': 'User not found'}, 404

api.add_resource(User, '/users', '/users/<string:user_id>')


if __name__ == "__main__":
    app.run(debug=True)