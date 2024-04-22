# Assuming you have a SECRET_KEY defined in your config
from loguru import logger

from server.services import (get_services)
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


def handle_get_services():
    success, message, services = get_services()
    if not success:
        return unified_response(False, message, code=500)
    return unified_response(True, message, data={"services": services}, code=200)