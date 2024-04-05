# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request
from loguru import logger

from server.handlers import (handle_create_user, handle_get_users, handle_get_user, handle_get_user_by_id, handle_update_user, handle_update_user_by_id, handle_delete_user, handle_delete_user_by_id)
from server.middlewares import rate_limit, user_token_required, admin_token_required

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["POST", "OPTIONS"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def create_user():
    """
    Registers a new user
    ---
    tags:
      - user
    description: Register a new user with the provided first name, last name, email, and password.
    parameters:
      - in: body
        name: body
        description: User's details
        required: true
        schema:
          type: object
          required:
            - first_name
            - last_name
            - email
            - password
          properties:
            first_name:
              type: string
              description: First name of the user.
            last_name:
              type: string
              description: Last name of the user.
            email:
              type: string
              description: Email address of the user
            password:
              type: string
              description: Password for the user's account
    responses:
      201:
        description: User registered successfully
      400:
        description: Validation error
      409:
        description: User already exists
      500:
        description: Internal server error
    """
    logger.info("Registering user")
    return handle_create_user(request.json)


@user_blueprint.route("/all", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def get_users(user):
    return handle_get_users(user)


@user_blueprint.route("/", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def get_user(user):
    return handle_get_user(user)


@user_blueprint.route("/<int:userId>", methods=["GET"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def get_user_by_id(user, userId):
    # Assuming 'handle_get_user' can accept a userId to fetch a specific user
    return handle_get_user_by_id(userId)


@user_blueprint.route("/", methods=["PUT"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def update_user(user):
    return handle_update_user(user, request.json)


@user_blueprint.route("/<int:userId>", methods=["PUT"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def update_user_by_id(user, userId):
    return handle_update_user_by_id(userId, request.json)


@user_blueprint.route("/", methods=["DELETE"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@user_token_required
def delete_user(user):
    return handle_delete_user(user)
  
  
@user_blueprint.route("/<int:userId>", methods=["DELETE"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@admin_token_required
def delete_user_by_id(user, userId):
    return handle_delete_user_by_id(userId)
