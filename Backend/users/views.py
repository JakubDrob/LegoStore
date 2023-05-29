from flask import Response
from flask_restful import Resource
from flask import request, make_response
from users.service import *
from utils.common import generate_response, TokenGenerator
from users.models import User


class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        input_data = request.get_json()

        print(input_data)
        response, status = create_user(request, input_data)
        return make_response(response, status)


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for login user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for forgot password email send user.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password_email_send(request, input_data)
        return make_response(response, status)


class ResetPassword(Resource):
    @staticmethod
    def post(token) -> Response:
        """
        POST response method for save new password.
        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)


class ShowUser(Resource):
    @staticmethod
    def get(user_id):
        user = get_user_by_id(user_id)
        if user:
            return {'user': user}, 200
        else:
            return {'message': 'User not found'}, 404
        
class GetAddress(Resource):
    @staticmethod
    def post():
        input_data = request.get_json()
        print(input_data)

        return get_user_address(input_data)

class SaveAddress(Resource):
    @staticmethod
    def post():
        input_data = request.get_json()
        print(input_data)

        # delete from input_data email that is in the end of the json, 
        # then create address in table and use email to connect it to the user
        #function save_user_address in service.py

        return save_user_address(input_data)

class GetProducts(Resource):
    @staticmethod
    def get():
        products = get_products()
        return {'products': products}, 200
    
class Health(Resource):
    @staticmethod
    def get():
        return {'health': 'ok'}, 200

class AddProduct(Resource):
    @staticmethod
    def post():
        
        input_data = request.get_json()
        # print(input_data)
        return add_product(input_data)

        # products = get_products()
        # return {'message': "ok"}, 200
    
