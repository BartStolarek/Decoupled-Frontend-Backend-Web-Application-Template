from loguru import logger
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app
import os

from server.models.user import User, Role


def get_new_token(user: User) -> tuple[bool, str, str]:
    
    if not user:
        logger.warning("User not provided")
        return False, "User not provided", ""
    
    user_id = user.id
    user_role = Role.query.filter_by(id=user.role_id).first().name
    
    # Get expiration time for the token from config.env
    try:
        expiration_time = int(os.getenv("TOKEN_EXPIRATION_TIME_SECONDS", 86400))
    except Exception:
        expiration_time = 86400
        logger.error("Error getting expiration time from config.env, set to 86400 seconds")
    
    token = jwt.encode(
        {
            "user_id": user_id,
            "user_role": user_role,
            "exp": datetime.utcnow() + timedelta(seconds=expiration_time)
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return True, "Token generated successfully", token


def login_user(email: str, password: str) -> tuple[bool, str, str]:
    try:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            # Find the role name associated with the user
            success, message, token = get_new_token(user)
            logger.info(f"User {email} authorized successfully")
            return success, message, token
        elif not check_password_hash(user.password_hash, password):
            logger.warning(
                f"Authorization failed for user {email}: Password is invalid")
            return False, 'Password is invalid', ''
        else:
            logger.warning(
                f"Authorization failed for user {email}: User does not exist")
            return False, 'User does not exist', ''
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return False, 'Unexpected error occurred', ''

