# Standard Imports
import datetime
import time

# Third Party Imports
from flask import Response, g, jsonify
from loguru import logger
from werkzeug.exceptions import BadRequest

# Local Imports
from server.utils.http_status_codes import HTTP_STATUS_CODES


def response_manipulator(response):
    """
    Manipulate the response before sending it to the client.
    """

    if hasattr(g, 'start_time'):
        response_time = f"{(time.time() - g.start_time) * 1000:.2f}ms"
    else:
        response_time = "Unavailable"

    # Prepare metadata
    metadata = {
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'responseTime': response_time
    }

    try:

        # response should be a jsonify object with the form:
        # jsonify({
        #   "status_code": 418,
        #   "data": data  (optional)
        # })

        if not isinstance(response, Response):
            raise BadRequest(
                "Response is not a Response object, ensure you are returning a jsonify object with a 'status_code' and optionally 'data'"
            )

        # Get the status code
        status_code = response.status_code

        # Check if there is a status if not get it from the HTTP status codes dictionary
        response.status = response.status if hasattr(
            response, 'status') else HTTP_STATUS_CODES.get(
                status_code, {}).get("status", "Couldn't obtain status")

        # Check if there is a message if not get it from the HTTP status codes dictionary
        response.message = response.message if hasattr(
            response, 'message') else HTTP_STATUS_CODES.get(
                status_code, {}).get("message", "Couldn't obtain message")
        response.metadata = metadata

        response.headers['Content-Type'] = 'application/json'
        response.headers[
            'X-Custom-Header'] = 'Custom Value'  # Replace with your custom headers

        return response

    except Exception as e:
        # Log the exception
        # TODO: Use logging framework to log this error, state in the log that
        print(e)
        print("print 3")
        # Use a generic error message for unexpected exceptions
        status_code = 500
        status = HTTP_STATUS_CODES.get(status_code,
                                       {}).get("status",
                                               "Couldn't obtain status")
        message = HTTP_STATUS_CODES.get(status_code, {}).get(
            "message", "An unexpected error occurred")

        error_response = jsonify({
            'status': status,
            'message': message,
            'metadata': metadata
        })
        error_response.status_code = status_code

        # Add headers
        error_response.headers['Content-Type'] = 'application/json'
        error_response.headers[
            'X-Custom-Header'] = 'Custom Value'  # Replace with your custom headers

        return error_response
