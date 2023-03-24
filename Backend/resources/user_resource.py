from flask_restful import Resource, reqparse
from database import get_user_by_id, get_user_by_username, add_user, update_user, delete_user
import os
from datetime import datetime, timedelta, timezone
import jwt

class User(Resource):
    def get(self, user_id):
        user = get_user_by_id(user_id)
        token = TokenGenerator.encode_token(user_id)
        user.update({'token': token})
        print(type(user))
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
class TokenGenerator:
    @staticmethod
    def encode_token(user_id):
        """
        The encode_token function takes in a user object and returns a token
        """

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "id": str(get_user_by_id(user_id)),
        }
        token = jwt.encode(payload, "this is a secret key", algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        """
        It takes a token, decodes it, and returns the decoded token

        :param token: The token to decode
        :return: A dictionary with the user's id and username.
        """
        return jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )

    @staticmethod
    def check_token(token):
        """
        It takes a token, and returns True if the token is valid, and False if it's not

        :param token: The token to be decoded
        :return: A boolean value.
        """
        try:
            jwt.decode(
                token,
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
                options={"require_exp": True},
            )
            return True
        except:
            return False

    @staticmethod
    def get_user_id(token):
        """
        It decodes the token, and returns the user's id

        :param token: The token that was sent to the server
        :return: The user id is being returned.
        """
        data = jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )
        return data["id"]


token_generator = TokenGenerator()