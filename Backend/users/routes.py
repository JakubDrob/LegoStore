from flask_restx import Api
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
    api.add_resource(UserShoppingCart, "/users/<string:user_id>/cart")
    api.add_resource(ChangeShoppingCartQuantity, "/users/<string:user_id>/cart/<string:product_id>/quantity")
    api.add_resource(Health, "/health")
    api.add_resource(AddProduct, "/addProduct")
    api.add_resource(SearchProducts,"/products/search/")

