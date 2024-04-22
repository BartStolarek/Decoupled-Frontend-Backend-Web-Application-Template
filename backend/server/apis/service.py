# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_get_services)
from server.middlewares import rate_limit, user_token_required, admin_token_required

service_blueprint = Blueprint("service", __name__)


@service_blueprint.route("/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def get_products():
    return handle_get_services()