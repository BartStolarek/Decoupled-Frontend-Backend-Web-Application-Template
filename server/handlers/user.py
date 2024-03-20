from datetime import datetime, timedelta

import jwt
# Assuming you have a SECRET_KEY defined in your config
from flask import current_app, request
from loguru import logger
from werkzeug.security import check_password_hash

from server.middlewares import token_required
from server.models import User  # Your User model
from server.schemas import UserSchema  # Your User schema
from server.services import (delete_user, get_user_details, register_user,
                             update_user)
from server.utils.http_status_codes import handle_status_code
from server.handlers.global_functions import check_not_success_message_and_get_code_and_response


def handle_register_user(request_data):
    # Function implementation

    user_schema = UserSchema()
    errors = user_schema.validate(request_data)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})

    else:
        user_data = user_schema.load(request_data)
        success, message = register_user(user_data)
        if success:
            logger.info(f"User registered successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            response, code = check_not_success_message_and_get_code_and_response(message)
    return response, code


def handle_authorize_user(request_data):

    email = request_data.get("email")
    password = request_data.get("password")

    if not email or not password:
        logger.error("Authorization failed: Email and password are required")
        code = 400
        response = handle_status_code(
            code, data={"error_info": "Email and password are required"})
        return response, code

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        try:
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "exp": datetime.utcnow() + timedelta(hours=1)
                },
                current_app.config["SECRET_KEY"],
                algorithm="HS256",
            )
            logger.info(f"User {email} authorized successfully")
            code = 200
            response = handle_status_code(code, data={"user_token": token})
            return response, code
        except Exception as e:
            logger.error(f"JWT encoding failed: {str(e)}")
            code = 500
            response = handle_status_code(
                code,
                data={
                    "error_info": "Internal server error during JWT encoding"
                })
            return response, code
    else:
        logger.warning(
            f"Authorization failed for user {email}: Invalid credentials")
        code = 401
        response = handle_status_code(
            code, data={"error_info": "Invalid credentials"})
        return response, code


def handle_delete_user(request_data):
    user_schema = UserSchema(only=["email"])
    errors = user_schema.validate(request_data)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code
    else:
        user_data = user_schema.load(request_data)
        success, message = delete_user(user_data)
        if success:
            logger.info(f"User deleted successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            logger.error(f"Conflict error: {message}")
            code = 409
            response = handle_status_code(code, data={"error_info": message})
        return response, code


def handle_update_user(request_data):
    user_schema = UserSchema(partial=True)
    errors = user_schema.validate(request_data)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code
    else:
        user_data = user_schema.load(request_data)
        success, message = update_user(user_data)
        if success:
            logger.info(f"User updated successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            if "Integrity Error: User with that email already exists" in message:
                logger.error(f"User already exists: {message}")
                code = 409
                response = handle_status_code(code,
                                              data={"error_info": message})
            else:
                logger.error(f"Internal server error: {message}")
                code = 500
                response = handle_status_code(code,
                                              data={"error_info": message})

        return response, code


def handle_user_details(current_user_id):
    try:
        success, message, user_details = get_user_details(current_user_id)
        if success:
            code = 200
            response = handle_status_code(code,
                                          data={"user_details": user_details})
            logger.info(
                f"User details retrieved successfully: {message}. {user_details}"
            )
        else:
            if message == "User does not exist":
                code = 400
                response = handle_status_code(code,
                                              data={"error_info": message})
                logger.error(f"User does not exist: {message}")
            else:
                code = 500
                response = handle_status_code(code,
                                              data={"error_info": message})
                logger.error(f"Internal server error: {message}")
    except Exception as e:
        logger.error(f"User details retrieval failed: {str(e)}")
        code = 500
        response = handle_status_code(
            code, data={"error_info": "Internal server error"})

    return response, code
