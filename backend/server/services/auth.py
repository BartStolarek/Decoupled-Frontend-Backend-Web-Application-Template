from loguru import logger
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app

from server.extensions import db
from server.models.user import User, Role


def login_user(email: str, password: str) -> tuple[bool, str, str]:
    try:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            # Find the role name associated with the user
            role_name = Role.query.filter_by(id=user.role_id).first().name
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "user_role": role_name,
                    "exp": datetime.utcnow() + timedelta(days=1)
                },
                current_app.config["SECRET_KEY"],
                algorithm="HS256",
            )
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

