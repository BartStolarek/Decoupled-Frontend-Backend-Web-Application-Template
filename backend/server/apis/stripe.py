# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_get_products, handle_get_services, handle_get_session_by_id)
from server.middlewares import rate_limit, user_token_required, admin_token_required

stripe_blueprint = Blueprint("stripe", __name__)


@stripe_blueprint.route("/product/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def get_products():
    return handle_get_products()


@stripe_blueprint.route("/service/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def get_service():
    return handle_get_services()

@stripe_blueprint.route("/session/<session_id>", methods=["GET"])
@rate_limit(50, 30)
@user_token_required
def get_session_by_id(user, session_id):
    return handle_get_session_by_id(user, session_id)

