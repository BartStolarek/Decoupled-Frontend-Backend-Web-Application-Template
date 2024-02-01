import os
import time

from dotenv import load_dotenv
from flask import Flask, g, jsonify
from flask_compress import Compress
from flask_login import LoginManager
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

from server.config import config as Config

from .middleware.api_logger import log_request, log_response
from .middleware.response_manipulator import response_manipulator
from .utils.http_status_codes import handle_status_code
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
    
    # Configuration for Flasgger before initializing it
    swagger_config = Swagger.DEFAULT_CONFIG
    
    # Trying to externally load static files
    swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
    swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
    swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
    swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'
    # Set swagger configuration
    swagger_config['title'] = 'AI Trainer API Documentation'
    swagger_config['uiversion'] = 3
    swagger_config['swagger_ui'] = True
    swagger_config['specs_route'] = '/apidocs/'
    swagger_config['favicon'] = '/static/favicon.ico'
    # swagger_config['base_url'] = '/api/v1' Include if you want to set a base URL for the API
    swagger_config['validate'] = False
    
    swagger = Swagger(server, config=swagger_config)

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
    # server.before_request(authenticate)
    server.after_request(response_manipulator)
    server.after_request(log_response)

    # Register blueprints
    from .api import server_blueprint as server_blueprint
    server.register_blueprint(server_blueprint, url_prefix='/server')
    from .api import user_blueprint as user_blueprint
    server.register_blueprint(user_blueprint, url_prefix='/user')

    # @server.route('/favicon.ico')
    # def favicon():
    #     return server.send_static_file('favicon.ico')

    @server.route('/test')
    def test_route():
        response = jsonify({"status_code": 200, "data": "Test data"})
        return response

    return server
