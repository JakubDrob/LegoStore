from flask import Flask, url_for, jsonify, request
from flask_restful import Api
from resources.user_resource import User
from resources.product_resource import Product
from resources.set_resource import Set
from flask_cors import CORS
from database import get_user_by_email, create_user
from TokenGenerator import TokenGenerator
from http import HTTPStatus
import hashlib

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(User, '/users', '/users/<string:user_id>')
api.add_resource(Product, '/products')
api.add_resource(Set, '/sets')

#------------------------------------------------------------------------------------------
# Route end points just for testing purposes, to be moved after refactorization of the code
#------------------------------------------------------------------------------------------
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']

    db_response = get_user_by_email(email)

    if(db_response is not None):
        return jsonify({'msg':"User with this email aready exists"}),HTTPStatus.CONFLICT

    salt = "abcd1234"
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()[:50]
    
    create_user(email, hashed_password)
    return jsonify({'msg':"User has been created"}),HTTPStatus.CREATED



@app.route('/login', methods=['POST'])
def login():
    # get email and password from request body
    email = request.json['email']
    password = request.json['password']

    db_response = get_user_by_email(email)

    if(db_response is None):
        return jsonify({'msg':"User with this email does not exists"}),HTTPStatus.FORBIDDEN

    user = {
        'id':db_response[0],
        'emial':db_response[2],
        'password':db_response[3]
    }

    salt = "abcd1234"
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()[:50]

    if(user):
        if(user['password']== hashed_password):
            token = TokenGenerator.encode_token(user['id'])
            user.update({'token': token})
            return jsonify({'user': user}), HTTPStatus.OK
        else:
            return jsonify({'msg':"Wrong password"}),HTTPStatus.UNAUTHORIZED
    else:
        print(user)
        return jsonify({'msg':"Error"}),HTTPStatus.NOT_FOUND
        
        
if __name__ == "__main__":
    app.run(debug=True)
