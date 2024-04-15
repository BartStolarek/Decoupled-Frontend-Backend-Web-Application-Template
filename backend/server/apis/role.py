# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_get_roles)
from server.middlewares import rate_limit, user_token_required, admin_token_required

role_blueprint = Blueprint("role", __name__)


@role_blueprint.route("/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def get_roles(user):
    return handle_get_roles(user)