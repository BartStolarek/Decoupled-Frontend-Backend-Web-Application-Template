# Assuming you have a SECRET_KEY defined in your config
from loguru import logger

from server.schemas import UserSchema  # Your User schema
from server.services import (create_user, get_users, get_user_by_id, update_user, update_user_by_id, delete_user, delete_user_by_id)
from server.models import User
from server.utils.http_status_codes import handle_status_code
from server.handlers.global_functions import check_not_success_message_and_get_code_and_response


# Utility for validating schemas
def validate_schema(data, schema, partial=False):
    schema_instance = schema(partial=partial)
    errors = schema_instance.validate(data)
    if errors:
        error_messages = [f"{field}: {', '.join(errors)}" for field, errors in errors.items()]
        logger.error(f"Schema validation failed: {', '.join(error_messages)}")
        return False, error_messages
    return True, schema_instance.load(data)


# Unified response handler
def unified_response(success: bool, message: str, data=None, code=500):
    if success:
        if data:
            return handle_status_code(code, data=data)
        return handle_status_code(code, data={"info": message})
    else:
        logger.error(message)
        response, code = check_not_success_message_and_get_code_and_response(message)
        return response, code


def handle_create_user(request_data):
    valid, data_or_errors = validate_schema(request_data, UserSchema)
    if not valid:
        return unified_response(False, "Failed to create user. Provided data was not valid.", data={"error_info": data_or_errors}, code=400)
    
    success, message = create_user(data_or_errors)  # data_or_errors contains loaded data if valid
    return unified_response(success, message, data={"info": message}, code=201 if success else 500)


def handle_get_users(user):
    if user.is_admin():
        success, message, users = get_users()
        user_dict_list = [user.to_dict() for user in users]
        if not success:
            return unified_response(False, message, code=500)
        return unified_response(True, message, data={"users": user_dict_list}, code=200)
    
    
def handle_get_user(user):
    if not isinstance(user, User):
        return unified_response(False, 'User not found', code=404)
    else:
        return unified_response(True, 'Success', data={"user": user.to_dict()}, code=200)


def handle_get_user_by_id(userId):
    success, message, user = get_user_by_id(userId)
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"user": user.to_dict()}, code=200)


def handle_update_user(user, request_data):
    if "password" in request_data:
        # If there's an attempt to directly update the password, return an error response
        return unified_response(False, "Password updates are not allowed here. Please use the dedicated password update endpoint.", code=400)
    
    valid, data_or_errors = validate_schema(request_data, UserSchema, partial=True)
    if not valid:
        return unified_response(False, "Failed to update user. Provided data was not valid.", data={"error_info": data_or_errors}, code=400)
    
    success, message, user = update_user(user, data_or_errors)
    return unified_response(success, message, data={"user": user.to_dict()}, code=200 if success else 500)


def handle_update_user_by_id(userId, request_data):
    if "password" in request_data:
        # If there's an attempt to directly update the password, return an error response
        return unified_response(False, "Password updates are not allowed here. Please use the dedicated password update endpoint.", code=400)
    
    valid, data_or_errors = validate_schema(request_data, UserSchema, partial=True)
    if not valid:
        return unified_response(False, "Failed to update user. Provided data was not valid.", data={"error_info": data_or_errors}, code=400)
    
    success, message, user = update_user_by_id(userId, data_or_errors)
    if not success:
        return unified_response(False, message, code=500)
    
    return unified_response(success, message, data={"user": user.to_dict()}, code=200 if success else 500)


def handle_delete_user(user):
    success, message, user = delete_user(user)
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"info": message}, code=200)


def handle_delete_user_by_id(userId):
    success, message = delete_user_by_id(userId)
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"info": message}, code=200)
