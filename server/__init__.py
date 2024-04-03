import os
import time

from dotenv import load_dotenv
from flasgger import Swagger
from flask import Flask, g, jsonify
from flask_compress import Compress
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy

from server.config import config as Config
from server.extensions import compress, db, login_manager, mail

from .middlewares.api_logger import log_request, log_response
from .middlewares.response_manipulator import response_manipulator
from .middlewares.preflight import handle_preflight
from .utils.flasgger import setup_flasgger
from .utils.http_status_codes import handle_status_code
from .utils.logger import setup_logger


def create_server(config_name=None):
    print('Starting initialisation of server')
    load_dotenv('config.env')
    server = Flask(__name__, static_folder='static')

    # Apply the custom preflight handling middleware by calling it with the server
    handle_preflight(server)  # Adjust this line to correctly apply your middleware

    
    
    frontend_origin = os.getenv('FRONTEND_ORIGIN', 'http://localhost:3000')
    CORS(server,
         supports_credentials=True,
         origins=[frontend_origin],
         methods=["GET", "POST", "OPTIONS"],
         allow_headers=[
             'Content-Type', 'Authorization', 'ngrok-skip-browser-warning'
         ])

    swagger = setup_flasgger(server)

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
    if not server.debug and not server.testing and not server.config[
            'SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(server)

    # Set up logger
    setup_logger()

    @server.before_request
    def before_request():
        # Store the start time in Flask's global `g` object
        g.start_time = time.time()

    @server.errorhandler(404)
    def page_not_found(e):
        response, code = handle_status_code(404)
        return response, code

    # Register middleware
    server.before_request(log_request)
    server.after_request(response_manipulator)
    server.after_request(log_response)

    # Register blueprints
    from .apis import server_blueprint as server_blueprint
    server.register_blueprint(server_blueprint, url_prefix='/server')
    from .apis import user_blueprint as user_blueprint
    server.register_blueprint(user_blueprint, url_prefix='/user')

    @server.route('/favicon.ico')
    def favicon():
        return server.send_static_file('favicon.ico')

    @server.route('/', methods=['GET'])
    def index():
        """
        Index endpoint for the server.
        """
        return "Welcome to the Flask Server!"

    @server.route('/test')
    def test_route():
        response = jsonify({"status_code": 200, "data": "Test data"})
        return response

    return server
