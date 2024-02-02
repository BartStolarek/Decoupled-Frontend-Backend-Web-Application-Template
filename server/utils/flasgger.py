# server/utils/swagger.py
from flasgger import Swagger, LazyJSONEncoder
from flask import request

def setup_flasgger(server):
    server.json_encoder = LazyJSONEncoder

    template = {
        "swagger": "2.0",
        "info": {
            "title": "My API",
            "description": "API for managing users",
            "contact": {
                "responsibleOrganization": "My Organization",
                "responsibleDeveloper": "Developer Name",
                "email": "developer@example.com",
                "url": "https://www.example.com",
            },
            "termsOfService": "https://www.example.com/terms",
            "version": "1.0.0"
        },
        "host": "mysite.com",  # This would be your production API host
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "getmyData"
    }

    # Configuration for Flasgger before initializing it
    swagger_config = Swagger.DEFAULT_CONFIG
    
    # Trying to externally load static files
    swagger_config['swagger_ui_bundle_js'] = 'https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
    swagger_config['swagger_ui_standalone_preset_js'] = 'https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
    swagger_config['jquery_js'] = 'https://unpkg.com/jquery@2.2.4/dist/jquery.min.js'
    swagger_config['swagger_ui_css'] = 'https://unpkg.com/swagger-ui-dist@3/swagger-ui.css'

    # Set swagger configuration
    swagger_config['title'] = 'AI Trainer API Documentation'
    swagger_config['uiversion'] = 3
    swagger_config['swagger_ui'] = True
    swagger_config['specs_route'] = '/apidocs/'
    swagger_config['favicon'] = '/static/favicon.ico'
    # swagger_config['base_url'] = '/api/v1' Include if you want to set a base URL for the API
    swagger_config['validate'] = False

    return Swagger(server, template=template, config=swagger_config)
