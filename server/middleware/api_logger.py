# Standard Imports

# Third Party Imports
from flask import request
from loguru import logger
from flask import Response

# Local Imports


def log_request():
    """Log details of the request"""
    # Check if the request is a CORS preflight request
    if request.method == "OPTIONS" and "Access-Control-Request-Method" in request.headers:
        logger.info(f"Preflight CORS request: {request.method} {request.path}")
    else:
        logger.info(f"Request: {request.method} {request.path}")
    # Add more details as needed


def log_response(response):
    """Log details of the response."""
    # Check if the response is to a CORS preflight request
    if request.method == "OPTIONS":
        preflight_info = "Preflight CORS response"
        logger.info(f"{preflight_info}: {response.status}")
    else:
        # Ensure response is a Flask Response object and not a Werkzeug BaseResponse, which may be in direct passthrough mode
        if isinstance(response, Response):
            try:
                # Attempt to access response.data safely
                max_length = 500
                truncated_data = response.get_data()[:max_length]

                if len(response.get_data()) > max_length:
                    truncated_data += b"... [Truncated]"

                # Decode the bytes to a string, assuming UTF-8 encoding. Adjust the encoding if needed.
                decoded_data = truncated_data.decode('utf-8', errors='replace')

                logger.info(
                    f"Response: {response.status}, Data: {decoded_data}"
                )
            except RuntimeError as e:
                # Handle cases where the response is in direct passthrough mode
                logger.error(f"Error logging response data: {e}")
                logger.info(
                    f"Response: {response.status} [Data not accessible]"
                )
        else:
            # If response is not a Flask Response object (e.g., direct passthrough mode), log without trying to access data
            logger.info(
                f"Response: {response.status} [Direct passthrough mode]"
            )
    return response
