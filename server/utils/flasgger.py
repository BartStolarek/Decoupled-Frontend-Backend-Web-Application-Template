# server/utils/swagger.py
from flasgger import Swagger, LazyJSONEncoder
from flask import request

def setup_flasgger(server):
    server.json_encoder = LazyJSONEncoder

    # Define the Swagger UI template
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
        "operationId": "getmyData",
        "externalDocs": {
            "description": "Find more info here",
            "url": "https://www.example.com/externalDocs"
        },
        # Add favicon to the template
        "favicon": "/static/favicon.ico",
    }

    # Define the Flasgger configuration
    swagger_config = {
        'headers': [],
        'specs': [
            {
                'endpoint': 'apispec_1',
                'route': '/apispec_1.json',
                'rule_filter': lambda rule: True,  # all in
                'model_filter': lambda tag: True,  # all in
            }
        ],
        'static_url_path': '/flasgger_static',
        'swagger_ui': True,
        'specs_route': '/apidocs/'
    }

    # Initialize Flasgger with the server, template, and configuration
    return Swagger(server, template=template, config=swagger_config)
