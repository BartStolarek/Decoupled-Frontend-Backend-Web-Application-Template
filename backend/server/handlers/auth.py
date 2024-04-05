from datetime import datetime, timedelta

import jwt
# Assuming you have a SECRET_KEY defined in your config
from flask import current_app, request
from loguru import logger
from werkzeug.security import check_password_hash

from server.models import User, Role  # Your User model
from server.schemas import UserSchema  # Your User schema
from server.services import login_user
from server.utils.http_status_codes import handle_status_code
from server.handlers.global_functions import check_not_success_message_and_get_code_and_response


def handle_login(request_data):
    email = request_data.get("email")
    password = request_data.get("password")

    if not email or not password:
        logger.error("Authorization failed: Email and password are required")
        code = 400
        response = handle_status_code(
            code, data={"error_info": "Email and password are required"})
        return response, code

    success, message, token = login_user(email, password)
    
    if success:
        code = 200
        response = handle_status_code(code, data={"info": message, "user_token": token})
        return response, code
    else:
        code = 401
        response = handle_status_code(code, data={"error_info": message})
        return response, code
    

def handle_logout(request_data):
    # TODO: Implement logout functionality for backend (i.e. remove token)
    pass


def handle_forgot_password(request_data):
    # TODO: Implement forgot password email generation
    pass


def handle_reset_password(request_data):
    # TODO: Implement password reset functionality with token/pass phrase input by user
    pass