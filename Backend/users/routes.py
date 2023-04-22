from flask_restful import Api
from users.views import *


def create_authentication_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(ShowUser, '/users', '/users/<string:user_id>')
    api.add_resource(SignUpApi, "/api/auth/register/")
    api.add_resource(LoginApi, "/api/auth/login/")
    api.add_resource(GetAddress, "/api/cart/getAddress/")
    api.add_resource(SaveAddress, "/api/cart/saveAddress/")
    api.add_resource(ForgotPassword, "/api/auth/forgot-password/")
    api.add_resource(ResetPassword, "/api/auth/reset-password/<token>")
    api.add_resource(GetProducts, "/products")