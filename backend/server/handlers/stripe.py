# Assuming you have a SECRET_KEY defined in your config
from loguru import logger

from server.services import (get_products, get_services, get_session_by_id)
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


def handle_get_products():
    success, message, products = get_products()
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"products": products}, code=200)


def handle_get_services():
    success, message, services = get_services()
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"services": services}, code=200)


def handle_get_session_by_id(user, session_id):
    
    success, message, session = get_session_by_id(session_id=session_id)
    
    if not success:
        logger.warning(f"Failed to fetch session: {message}")
        return unified_response(success, message, code=500)
    
    # Check if session belongs to user
    if user.is_admin():
        logger.info(f"Admin user {user.email} fetched session: {session_id}")
        return unified_response(success, message, data={"session": session}, code=200)
    
    if session.get('customer_email') != user.email:
        logger.error(f"User {user.email} is not authorised to access this session: {session_id} which is for user {session.get('customer_email')}")
        return unified_response(False, 'Unauthorised to access this session', code=404)

    logger.info(f"User {user.email} fetched session: {session_id}")
    return unified_response(True, message, data={"session": session}, code=200)