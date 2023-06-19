"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask, jsonify
from flask_mail import Mail
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from users.models import User
from database import db
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate
from flask_restx import Api

#db = SQLAlchemy()
# mail = Mail()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)

    

    # This is the configuration for the email server.
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_HOST_USER")
    app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_HOST_PASSWORD")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    # Configuration for db
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

    app.config.from_object("config.Config")


    api = Api(app, version='1.0', title='Lego API', description='A Lego API',)
    from users.routes import create_authentication_routes

    create_authentication_routes(api=api)
    #
    db.init_app(app)

    migrate = Migrate(app, db)

    with app.app_context():

        # db.create_all()  # Create database tables for our data models

        return app
    
app = create_app();

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)