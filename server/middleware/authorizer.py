from datetime import datetime, timezone
from functools import wraps
from flask import request, jsonify, current_app
import jwt
from loguru import logger
from jwt import ExpiredSignatureError, InvalidTokenError

from server.services.user import get_users
from server.utils.http_status_codes import handle_status_code

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logger.info("Checking if token is valid")
        token = None

        # Check if the token is in the request headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        # Return 401 if token is not passed
        if not token:
            logger.error("Failed to access endpoint, token is missing!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Token is missing!"})
            return response, 401

        try:
            # Decode the token
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            
            # Get current UTC time as Unix timestamp
            current_utc_timestamp = datetime.now(timezone.utc).timestamp()
            
            # Check if token is expired
            if data['exp'] < current_utc_timestamp:
                logger.error("Failed to access endpoint, token has expired!")
                code = 401
                response = handle_status_code(code, data={"error_info": "Failed to access endpoint, token has expired!"})
                return response, 401
            
            users = get_users("id", data['user_id'])
            if not users:
                logger.error("Failed to access endpoint, user does not exist!")
                code = 401
                response = handle_status_code(code, data={"error_info": "Failed to access endpoint, user does not exist!"})
                return response, 401
            else:
                current_user_id = users[0].id
                
        except ExpiredSignatureError:
            logger.error("Failed to access endpoint, token has expired!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Failed to access endpoint, token has expired!"})
            return response, 401
        except InvalidTokenError:
            logger.error("Failed to access endpoint, token is invalid!")
            code = 401
            response = handle_status_code(code, data={"error_info": "Failed to access endpoint, token is invalid!"})
            return response, 401
        except Exception as e:
            logger.error(f"Failed to access endpoint: Error type: {type(e)}, Error: {e}")
            code = 500
            response = handle_status_code(code, data={"error_info": "Failed to access endpoint - server error"})
            return response, 500

        return f(current_user_id, *args, **kwargs)

    return decorated_function
