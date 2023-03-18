from flask_restful import Resource, reqparse
from database import get_user_by_id, get_user_by_username, add_user, update_user, delete_user


class User(Resource):
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if user:
            return {'user': user}, 200
        else:
            return {'message': 'User not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username is required', required=True)
        parser.add_argument('password', type=str, help='Password is required', required=True)
        args = parser.parse_args()

        # Check if username already exists
        user = get_user_by_username(args['username'])
        if user:
            return {'message': 'Username already exists'}, 409

        # Insert new user
        user_id = add_user(args['username'], args['password'])
        return {'message': 'User created', 'user_id': user_id}, 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username is required', required=True)
        parser.add_argument('password', type=str, help='Password is required', required=True)
        args = parser.parse_args()

        # Check if user exists
        user = get_user_by_id(user_id)
        if user:
            update_user(user_id, args['username'], args['password'])
            return {'message': 'User updated', 'user_id': user_id}, 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        # Delete user
        user = get_user_by_id(user_id)
        if user:
            delete_user(user_id)
            return {'message': 'User deleted'}, 200
        else:
            return {'message': 'User not found'}, 404
