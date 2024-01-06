import os
import time
from flask import Flask, g, jsonify
from flask_compress import Compress
from flask_login import LoginManager
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy
from server.config import config as Config
from dotenv import load_dotenv
from .middleware.api_logger import log_request, log_response
from .middleware.response_manipulator import response_manipulator
from .middleware.authorizer import authenticate
from .utils.logger import setup_logger

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
compress = Compress()

def create_server(config_name=None):
    print('Starting initialisation of server')
    load_dotenv('config.env')
    server = Flask(__name__)

    if not config_name:
        config_name = os.getenv('FLASK_CONFIG', 'default')

    server.config.from_object(Config[config_name])
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Config[config_name].init_app(server)

    # Set up extensions
    db.init_app(server)
    login_manager.init_app(server)
    mail.init_app(server)
    compress.init_app(server)
    RQ(server)

    # Configure SSL if platform supports it
    if not server.debug and not server.testing and not server.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(server)
    
    # Set up logger
    setup_logger()
    
    @server.before_request
    def before_request():
        # Store the start time in Flask's global `g` object
        g.start_time = time.time()
    
    # Register middleware
    server.before_request(log_request)
    #server.before_request(authenticate)
    server.after_request(response_manipulator)
    server.after_request(log_response)
    
    # Register blueprints
    from .api import server as server_blueprint
    server.register_blueprint(server_blueprint, url_prefix='/api')

    @server.route('/test')
    def test_route():
        response = jsonify({"status_code": 200, "data": "Test data"})
        return response

    
    return server


