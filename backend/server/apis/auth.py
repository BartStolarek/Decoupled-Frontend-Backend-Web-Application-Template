# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_login, handle_admin, handle_user, handle_refresh, handle_logout, handle_forgot_password, handle_reset_password)
from server.middlewares import rate_limit, admin_token_required, user_token_required

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["POST", "OPTIONS"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def login():
    return handle_login(request.json)


@auth_blueprint.route("/admin", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def admin(user):
    logger.info(f"/admin route called by {user.email}")
    return handle_admin(user)


@auth_blueprint.route("/user", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def user(user):
    logger.info(f"/user route called by {user.email}")
    return handle_user(user)


@auth_blueprint.route("/refresh", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def refresh(user):
    logger.info(f"/refresh route called by {user.email}")
    return handle_refresh(user)


@auth_blueprint.route("/logout", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def logout(user):
    return handle_logout(user)


@auth_blueprint.route("/forgot-password", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def forgot_password():
    return handle_forgot_password(request.json)
  
  
@auth_blueprint.route("/reset-password", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def reset_password():
    return handle_reset_password(request.json)
