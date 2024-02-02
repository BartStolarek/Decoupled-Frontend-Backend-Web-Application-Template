# Standard Imports
import datetime
import time

# Third Party Imports
from flask import Response, jsonify, g
from loguru import logger
from werkzeug.exceptions import BadRequest

# Assuming HTTP_STATUS_CODES is a dictionary mapping status codes to messages
from server.utils.http_status_codes import HTTP_STATUS_CODES

def response_manipulator(response):
    if response.content_type == 'application/json':
        if hasattr(g, 'start_time'):
            response_time = f"{(time.time() - g.start_time) * 1000:.2f}ms"
        else:
            response_time = "Unavailable"

        metadata = {
            'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
            'responseTime': response_time
        }

        try:
            if not isinstance(response, Response):
                raise BadRequest("Expected a Flask `Response` object.")

            # Ensure response status and message are set based on HTTP_STATUS_CODES
            status_code = response.status_code
            if status_code in HTTP_STATUS_CODES:
                status_detail = HTTP_STATUS_CODES[status_code]
                # Inject status and message into the response JSON if necessary
                # This step depends on how you structure your JSON responses
                # Example: Modify response.json to include status and message
            response.headers['Content-Type'] = 'application/json'
            response.headers['X-Custom-Header'] = 'Custom Value'
            return response
        except Exception as e:
            logger.error(f"Error manipulating response: {e}")
            # Fallback for errors during manipulation
            status_code = 500
            status_detail = HTTP_STATUS_CODES.get(status_code, {"message": "Internal Server Error"})
            error_response = jsonify({
                'status': status_code,
                'message': status_detail["message"],
                'metadata': metadata
            })
            error_response.status_code = status_code
            error_response.headers['Content-Type'] = 'application/json'
            error_response.headers['X-Custom-Header'] = 'Custom Value'
            return error_response
    else:
        return response
