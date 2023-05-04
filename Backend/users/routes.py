from flask_restful import Api
from users.views import LoginApi, ForgotPassword, SignUpApi, ResetPassword, ShowUser


def create_authentication_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(ShowUser, '/users', '/users/<string:user_id>')
    api.add_resource(SignUpApi, "/api/auth/register/")
    api.add_resource(LoginApi, "/api/auth/login/")
    api.add_resource(ForgotPassword, "/api/auth/forgot-password/")
    api.add_resource(ResetPassword, "/api/auth/reset-password/<token>")