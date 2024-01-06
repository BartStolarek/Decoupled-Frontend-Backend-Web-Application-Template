# Standard Imports

# Third Party Imports
from loguru import logger
from flask import request

# Local Imports


def log_request():
    """ Log details of the request """
    print("print in log request log request")
    logger.info(f"Request: {request.method} {request.path}")
    # You can add more details as needed
    

def log_response(response):
    """ Log details of the response """
    if hasattr(response, "data"):
        max_length = 200
        truncated_data = response.data[:max_length]
        
        if len(response.data) > max_length:
            truncated_data += b"... [Truncated]"
        
        # Decode the bytes to a string, assuming UTF-8 encoding. Adjust the encoding if needed.
        decoded_data = truncated_data.decode('utf-8', errors='replace')
        
        logger.info(f"Response: {response.status_code} {response.status} {response.message} {decoded_data}")
        return response
    else:
        logger.info(f"Response: {response.status_code}  {response.status} {response.message}")
