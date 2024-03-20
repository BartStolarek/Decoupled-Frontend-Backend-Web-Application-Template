from server.utils.http_status_codes import handle_status_code
from typing import Tuple
from loguru import logger
from flask import jsonify


def check_not_success_message_and_get_code_and_response(message: str) -> Tuple[jsonify, int]:
    if message == "User does not exist":
        code = 400
        response = handle_status_code(code, data={"error_info": message})
        logger.error(f"User does not exist: {message}")
    elif "Integrity Error: User with that email already exists" in message:
        logger.error(f"User already exists: {message}")
        code = 409
        response = handle_status_code(code, data={"error_info": message})
    else:
        code = 500
        response = handle_status_code(code, data={"error_info": message})
        logger.error(f"Internal server error: {message}")
    return response, code
