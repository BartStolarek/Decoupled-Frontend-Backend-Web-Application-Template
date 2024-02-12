# Standard Imports
import datetime
import time
import os

# Third Party Imports
from flask import Response, jsonify, g
from loguru import logger
from werkzeug.exceptions import BadRequest

# Assuming HTTP_STATUS_CODES is a dictionary mapping status codes to messages
from server.utils.http_status_codes import HTTP_STATUS_CODES

def calculate_response_time():
    if hasattr(g, 'start_time'):
        return f"{(time.time() - g.start_time) * 1000:.2f}ms"
    return "Unavailable"

def append_metadata(response, metadata):
    # Add metadata to response headers or body as needed
    response.headers['X-Response-Time'] = metadata['responseTime']
    response.headers['X-Timestamp'] = metadata['timestamp']

def handle_cors_headers(response, frontend_origin):
    response.headers['Access-Control-Allow-Origin'] = frontend_origin  # or a specific domain
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,ngrok-skip-browser-warning'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


def create_error_response(status_code, message, metadata):
    response = jsonify({
        'status': status_code,
        'message': message,
        'metadata': metadata
    })
    response.status_code = status_code
    return response

def response_manipulator(response):
    metadata = {
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'responseTime': calculate_response_time()
    }

    try:
        append_metadata(response, metadata)
        frontend_origin = os.getenv('FRONTEND_ORIGIN', 'http://localhost:5000')  # Default value for development
        handle_cors_headers(response, frontend_origin)
    except Exception as e:
        logger.error(f"Error manipulating response: {e}")
        return create_error_response(500, "Internal Server Error", metadata)
    
    # Log response headers and status
    logger.debug(f"Response Headers: {response.headers}")
    logger.debug(f"Response Status: {response.status}")

    return response
