import json
import jwt
import datetime
from database import db
from os import environ
from users.helper import send_forgot_password_email
from users.models import *
from flask_bcrypt import generate_password_hash
from utils.common import generate_response, TokenGenerator
from users.validation import (
    CreateLoginInputSchema,
    CreateResetPasswordEmailSendInputSchema,
    CreateSignupInputSchema, ResetPasswordInputSchema,
)
from utils.http_code import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from config import Config
import base64
from io import BytesIO
import binascii
from azure.storage.blob import BlobServiceClient

def create_user(request, input_data):
    """
    It creates a new user
    :param request: The request object
    :param input_data: This is the data that is passed to the function
    :return: A response object
    """
    isAdmin = False

    check_email_exist = User.query.filter_by(email=input_data.get("email")).first()
    if check_email_exist:
        return generate_response(
            message="Email  already taken", status=HTTP_400_BAD_REQUEST
        )
    
    if (len(input_data['adminPassword']) != 0):
        if input_data['adminPassword'] != "12345":
            return generate_response(
                message="Wrong admin password", status=HTTP_400_BAD_REQUEST
            )
        else:
            isAdmin = True

    input_data['adminPassword'] = isAdmin
    new_user = User(**input_data)  # Create an instance of the User class
    new_user.hash_password()
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Comment

    print(new_user)
    del input_data["password"]
    return generate_response(
        data=input_data, message="User Created", status=HTTP_201_CREATED
    )


def login_user(request, input_data):
    """
    It checks if the user exists, checks if
    the password is correct, and returns a response
    :param request: The request object
    :param input_data: The data that is passed to the function
    :return: A dictionary with the keys: data, message, status
    """

    get_user = User.query.filter_by(email=input_data.get("email")).first()
    if get_user is None:
        return generate_response(message="User not found", status=HTTP_404_NOT_FOUND)
    if get_user.check_password(input_data.get("password")):
        token = jwt.encode(
            {
                "Userid": get_user.Userid,
                "email": get_user.email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            environ.get("SECRET_KEY"),
        )
        input_data["token"] = token

        if(get_user.isAdmin == True):
            input_data["admin"] = True
        else:
            input_data["admin"] = False


        return generate_response(
            data=input_data, message="User login successfully", status=HTTP_201_CREATED
        )
    else:
        return generate_response(
            message="Password is wrong", status=HTTP_401_UNAUTHORIZED
        )


def reset_password_email_send(request, input_data):
    """
    It takes an email address as input, checks if the email address is registered in the database, and
    if it is, sends a password reset email to that address
    :param request: The request object
    :param input_data: The data that is passed to the function
    :return: A response object with a message and status code.
    """
    create_validation_schema = CreateResetPasswordEmailSendInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    user = User.query.filter_by(email=input_data.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with this email. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    send_forgot_password_email(request, user)
    return generate_response(
        message="Link sent to the registered email address.", status=HTTP_200_OK
    )


def reset_password(request, input_data, token):
    create_validation_schema = ResetPasswordInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    if not token:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = TokenGenerator.decode_token(token)
    user = User.query.filter_by(Userid=token.get('Userid')).first()
    if user is None:
        return generate_response(
            message="No record found with this email. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    user = User.query.filter_by(Userid=token['Userid']).first()
    user.password = generate_password_hash(input_data.get('password')).decode("utf8")
    db.session.commit()
    return generate_response(
        message="New password SuccessFully set.", status=HTTP_200_OK
    )


def get_user_by_id(user_id):
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    users = User.query.filter_by(Userid=user_id).first()
    user_dicts = users.__dict__
    user_dicts.pop('_sa_instance_state', None)
    session.close()
    return user_dicts

def get_user_address(user_email):
    user = User.query.filter_by(email=user_email).first()

    print(user.Address)
    if user is None or user.Address is None:
        
        return generate_response(
        message="User has no address saved", status=HTTP_404_NOT_FOUND
    )
    
    print(user)
    print(user.Address)

    user_address_id = user.Address
    user_address = Address.query.filter_by(AddressID=user_address_id).first()
    print(type(user_address))
    print(type(user_email))
    json_address = {
        "FirstName": user_address.FirstName,
        "LastName": user_address.LastName,
        "Country": user_address.Country,
        "City": user_address.City,
        "StreetName": user_address.StreetName,
        "StreetNo": user_address.StreetNo,
        "AppartmentNo": user_address.AppartmentNo,
        "PostCode": user_address.PostCode
    }
    
    return generate_response(
    data=json_address, message="User address found", status=HTTP_202_ACCEPTED)
        
def save_user_address(input_data):
        
        user_email = input_data.get("Email")
        del input_data["Email"]

        #Find user with this emial
        user = User.query.filter_by(email=user_email).first()
        print(user.Userid)

        if(user.Address is None):
            print("[save_user_address] there is no address to be deleted")
        else:
            #Find current address saved in db and delete it
            oldAddress = Address.query.filter_by(AddressID=user.Address).first()
            db.session.delete(oldAddress)
            db.session.commit()
            #Delete also address from user
            user.Address = None
            db.session.commit()


        #Save to DB new address
        new_user_address = Address()  # Create an instance of the User class
        new_user_address = Address()
        new_user_address.FirstName = input_data.get("FirstName")
        new_user_address.LastName = input_data.get("LastName")
        new_user_address.StreetName = input_data.get("StreetName")
        new_user_address.StreetNo = input_data.get("StreetNo")
        new_user_address.AppartmentNo = input_data.get("AppartmentNo")
        new_user_address.PostCode = input_data.get("PostCode")
        new_user_address.City = input_data.get("City")
        new_user_address.Country = input_data.get("Country")

        print(new_user_address)

        db.session.add(new_user_address)  # Adds new User record to database
        db.session.commit()  # Comment

        last_address = Address.query.order_by(Address.AddressID.desc()).first()

        #connect address to the user
        user.Address = last_address.AddressID
        db.session.commit()

def get_products():

    result =  Product.query.all()
    converted_result = []
    for row in result:
        image = read_blob(row.Image)

        dict_row = {'id': row.ProductID,
                    'name': row.Name,
                    'set_no': row.SetNo,
                    'price': row.Price,
                    'description': row.Description,
                    'image': image.decode("utf-8"),
                    'availability': row.Availability,
                    'release_date': datetime.datetime.strftime(row.ReleaseDate, "%Y-%m-%d"),
                    'piece_count': row.PieceCount,
                    'product_type_id': row.ProductTypeID}
        converted_result.append(dict_row)
    return converted_result

def get_user_shopping_cart(user_id: int):
    
    user: User = User.query.filter_by(Userid=user_id).first()

    result = ShoppingCartItem.query.filter_by(ShoppingCartId=user.ShoppingCartID).all()

    converted_result = []
    for row in result:
        product = Product.query.filter_by(ProductID=row.ProductId).first()
        image = read_blob(product.Image)
        dict_row = {
            'productId': product.ProductID,
            'title': product.Name,
            'quantity': row.Quantity,
            'image': image.decode("utf-8"),
            'price': product.Price
        }
        converted_result.append(dict_row)
    return converted_result

def increase_shopping_cart_quantity(user_id: int, product_id: int):
    user: User = User.query.filter_by(Userid=user_id).first()

    result: ShoppingCartItem = ShoppingCartItem.query.filter_by(ShoppingCartId=user.ShoppingCartID, ProductId=product_id).first()

    result.Quantity += 1

    db.session.commit()

def decrease_shopping_cart_quantity(user_id: int, product_id: int):
    user: User = User.query.filter_by(Userid=user_id).first()

    result: ShoppingCartItem = ShoppingCartItem.query.filter_by(ShoppingCartId=user.ShoppingCartID, ProductId=product_id).first()

    if(result.Quantity == 1):
        db.session.delete(result)
    result.Quantity -= 1

    db.session.commit()

def add_product_to_shopping_cart(user_id: int, product_id: int):
    user: User = User.query.filter_by(Userid=user_id).first()

    cart_item = ShoppingCartItem()
    cart_item.ProductId = product_id,
    cart_item.ShoppingCartId = user.ShoppingCartID
    cart_item.Quantity = 1

    db.session.add(cart_item)

    db.session.commit()
def add_product(input_data):
    
    # blob = base64_to_blob(input_data["Image"])

    upload_image(input_data["Image"], input_data["Name"])

    input_data["Image"] = input_data["Name"]

    new_product = Product(**input_data)  # Create an instance of the User class
    db.session.add(new_product)  # Adds new User record to database
    db.session.commit()  # Comment

    return generate_response(
    data=input_data, message="Product Created", status=HTTP_201_CREATED
    )


def upload_image(image_file, file_name):
    blob_name = file_name

    # Azure Blob Storage connection string
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=csb1003200066accade;AccountKey=A5qnWwOWTe5pXK3M8RqS8YGFazGZW2NtIWDc+i1vJC1kPNAz3dFhNHYG15CuChAnh2OElpti5yjT+ASt7grt2A==;EndpointSuffix=core.windows.net'

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get the blob container
    container_name = 'blobs'
    container_client = blob_service_client.get_container_client(container_name)

    # Upload the image file as a blob
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(image_file)

    return 'Image uploaded successfully'

def read_blob(blob_name):
    # Azure Blob Storage connection string
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=csb1003200066accade;AccountKey=A5qnWwOWTe5pXK3M8RqS8YGFazGZW2NtIWDc+i1vJC1kPNAz3dFhNHYG15CuChAnh2OElpti5yjT+ASt7grt2A==;EndpointSuffix=core.windows.net'

    container_name = 'blobs'

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a reference to the blob container
    container_client = blob_service_client.get_container_client(container_name)

    # Get a reference to the blob
    blob_client = container_client.get_blob_client(blob_name)

    # Download the blob
    blob_data = blob_client.download_blob()

    # Read the blob data
    blob_content = blob_data.readall()

    return blob_content

import json

def get_products_by_tag(tag_name):
    tag = Tag.query.filter_by(Name=tag_name).first()

    print("Found tag: ", tag.Name)

    if not tag:
        return []

    product_tag_ids = Product_Tag.query.filter_by(TagID=tag.TagID).all()
    product_ids = [pt.ProductID for pt in product_tag_ids]

    products = Product.query.filter(Product.ProductID.in_(product_ids)).all()

    print(products)
    converted_result = []
    for row in products:
        image = read_blob(row.Image)

        dict_row = {'id': row.ProductID,
                    'name': row.Name,
                    'set_no': row.SetNo,
                    'price': row.Price,
                    'description': row.Description,
                    'image': image.decode("utf-8"),
                    'availability': row.Availability,
                    'release_date': datetime.datetime.strftime(row.ReleaseDate, "%Y-%m-%d"),
                    'piece_count': row.PieceCount,
                    'product_type_id': row.ProductTypeID}

        converted_result.append(dict_row)

    return converted_result
