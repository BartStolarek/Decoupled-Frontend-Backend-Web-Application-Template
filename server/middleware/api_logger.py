# Standard Imports

# Third Party Imports
from flask import request
from loguru import logger
from flask import Response

# Local Imports


def log_request():
    """ Log details of the request """
    logger.info(f"Request: {request.method} {request.path}")
    # You can add more details as needed


def log_response(response):
    """ Log details of the response """
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
                f"Response: {response.status} {response.message if hasattr(response, 'message') else ''} {decoded_data}"
            )
        except RuntimeError as e:
            # Handle cases where the response is in direct passthrough mode
            logger.error(f"Error logging response data: {e}")
            logger.info(
                f"Response: {response.status} {response.message if hasattr(response, 'message') else ''} [Data not accessible]"
            )
    else:
        # If response is not a Flask Response object (e.g., direct passthrough mode), log without trying to access data
        logger.info(
            f"Response: {response.status} {response.message if hasattr(response, 'message') else ''} [Direct passthrough mode]"
        )
    return response

