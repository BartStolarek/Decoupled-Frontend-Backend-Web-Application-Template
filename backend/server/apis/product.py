# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_get_products)
from server.middlewares import rate_limit, user_token_required, admin_token_required

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def get_products():
    return handle_get_products()