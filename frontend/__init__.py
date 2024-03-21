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

from frontend.config import config as Config
from frontend.extensions import compress, db, login_manager, mail

from .utils.http_status_codes import handle_status_code
from .utils.logger import setup_logger


def create_frontend(config_name=None):
    print('Starting initialisation of frontend')
    load_dotenv('config.env')
    frontend = Flask(__name__, static_folder='static')

    server_origin = os.getenv('SERVER_ORIGIN', 'http://localhost:5000')
    CORS(frontend,
         supports_credentials=True,
         origins=[server_origin],
         methods=["GET", "POST", "OPTIONS"],
         allow_headers=[
             'Content-Type', 'Authorization', 'ngrok-skip-browser-warning'
         ])

    if not config_name:
        config_name = os.getenv('FLASK_CONFIG', 'default')

    frontend.config.from_object(Config[config_name])
    frontend.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Config[config_name].init_app(frontend)

    # Set up extensions
    login_manager.init_app(frontend)
    mail.init_app(frontend)
    compress.init_app(frontend)
    RQ(frontend)

    # Configure SSL if platform supports it
    if not frontend.debug and not frontend.testing and not frontend.config[
            'SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(frontend)

    # Set up logger
    setup_logger()

    @frontend.before_request
    def before_request():
        # Store the start time in Flask's global `g` object
        g.start_time = time.time()

    @frontend.errorhandler(404)
    def page_not_found(e):
        response, code = handle_status_code(404)
        return response, code
    
    @frontend.after_request
    def add_header(response):
        # If development, test environment
        if config_name in ['development', 'test']:
            response.cache_control.no_store = True
        return response  # Make sure to return the response object


    # Register blueprints
    from .pages import home_blueprint as home_blueprint
    frontend.register_blueprint(home_blueprint)
    from .pages import style_guide_blueprint as style_guide_blueprint
    frontend.register_blueprint(style_guide_blueprint)
    
    @frontend.route('/favicon.ico')
    def favicon():
        return frontend.send_static_file('favicon.ico')

    @frontend.route('/test')
    def test_route():
        response = jsonify({"status_code": 200, "data": "Test data"})
        return response

    return frontend
