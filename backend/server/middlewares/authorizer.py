from functools import wraps
from flask import request, jsonify
from loguru import logger
from server.utils.http_status_codes import handle_status_code
from server.services.user import get_user_by_id
import jwt
from flask import current_app
from jwt import ExpiredSignatureError, InvalidTokenError

def token_validation(f, require_admin=False):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logger.info("Checking if token is valid")
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            logger.error("Failed to access endpoint, token is missing!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Token is missing!"})
            return response, 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            success, message, user = get_user_by_id(user_id=data['user_id'])

            if not success or not user:
                logger.error("Failed to access endpoint, user does not exist!")
                code = 401
                response = handle_status_code(code, data={"error_info": "User does not exist!"})
                return response, 401

            if require_admin and not user.is_admin():
                logger.error("Failed to access endpoint, user is not an admin!")
                code = 403
                response = handle_status_code(code, data={"error_info": "Not authorized!"})
                return response, 403

        except ExpiredSignatureError:
            logger.error("Failed to access endpoint, token has expired!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Token has expired!"})
            return response, 401
        except InvalidTokenError:
            logger.error("Failed to access endpoint, token is invalid!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Token is invalid!"})
            return response, 401
        except Exception as e:
            logger.error(f"Failed to access endpoint: {e}")
            code = 500
            response = handle_status_code(code, data={"error_info": "Server error"})
            return response, 500

        # Inject user into the function arguments
        return f(user, *args, **kwargs)

    return decorated_function

def user_token_required(f):
    return token_validation(f, require_admin=False)

def admin_token_required(f):
    return token_validation(f, require_admin=True)
