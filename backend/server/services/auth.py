from loguru import logger
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app

from server.extensions import db
from server.models.user import User, Role

def get_new_token(user_id: int, user_role: str) -> str:
    token = jwt.encode(
        {
            "user_id": user_id,
            "user_role": user_role,
            "exp": datetime.utcnow() + timedelta(seconds=30)
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return token

def login_user(email: str, password: str) -> tuple[bool, str, str]:
    try:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            # Find the role name associated with the user
            role_name = Role.query.filter_by(id=user.role_id).first().name
            token = get_new_token(user.id, role_name)
            logger.info(f"User {email} authorized successfully")
            return True, 'User authorized successfully', token
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

