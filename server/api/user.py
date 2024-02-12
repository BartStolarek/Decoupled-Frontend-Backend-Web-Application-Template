from loguru import logger

# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, request

from server.middleware import rate_limit
from server.handler import handle_register_user, handle_authorize_user, handle_delete_user, handle_update_user, handle_user_details
from server.middleware import token_required

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/register", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def register():
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
            - date_of_birth
            - height_cm
            - weight_kg
            - gender
            - email
            - password
          properties:
            first_name:
              type: string
              description: First name of the user.
            last_name:
              type: string
              description: Last name of the user.
            date_of_birth:
              type: string
              description: Date of birth of the user.
            height_cm:
              type: string
              description: Height of the user.
            weight_kg:
              type: string
              description: Weight of the user.
            gender:
              type: string
              description: Gender of the user.
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
    return handle_register_user(request.json)

@user_blueprint.route("/authorize", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def authorize():
    """
    Authorize a user and return a JWT token.
    ---
    tags:
      - user
    description: Authorizes a user and returns a JWT token upon successful authentication.
    parameters:
      - in: body
        name: body
        description: User's login credentials.
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              description: Email address of the user.
            password:
              type: string
              description: Password of the user.
    responses:
      200:
        description: Successfully authenticated and token returned.
      400:
        description: Validation error, email and password are required.
      401:
        description: Unauthorized, invalid credentials provided.
    """
    logger.info("Authorizing user")
    return handle_authorize_user(request.json)


@user_blueprint.route("/delete", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@token_required
def delete():
    """
    Delete a user from the database.
    ---
    tags:
      - user
    description: Deletes a user with the given email from the database.
    parameters:
      - in: body
        name: body
        description: Email of the user to delete.
        required: true
        schema:
          type: object
          required:
            - email
          properties:
            email:
              type: string
              description: Email address of the user to be deleted.
    responses:
      201:
        description: User deleted successfully.
      400:
        description: Validation error or user does not exist.
      409:
        description: Conflict error if deletion conditions are not met.
    """
    logger.info("Deleting user")
    return handle_delete_user(request.json)


@user_blueprint.route("/update", methods=["POST"])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
@token_required
def update():
    """
    Update user details.
    ---
    tags:
      - user
    description: Updates details of an existing user.
    parameters:
      - in: body
        name: body
        description: User details to update.
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
              description: New first name of the user.
            last_name:
              type: string
              description: New last name of the user.
            email:
              type: string
              description: New email address of the user.
    responses:
      201:
        description: User updated successfully.
      400:
        description: Validation error or user does not exist.
      409:
        description: Conflict error if update conditions are not met.
      500:
        description: Internal server error.
    """
    logger.info("Updating user")
    return handle_update_user(request.json)


@user_blueprint.route("/user-details", methods=["GET"])
@rate_limit(50, 30)
@token_required
def user_details(current_user_id):
    """
    Retrieve the details of the currently logged-in user.
    ---
    tags:
        - user
    description: Retrieves details of the currently logged-in user based on their JWT token.
    parameters:
      - in: header
        name: Authorization
        description: Access token to authenticate the request. Should be formatted as 'Bearer <token>'.
        required: true
        schema:
          type: string
    responses:
      200:
        description: User details retrieved successfully. Returns user details.
      400:
        description: Bad request, such as missing or invalid token.
      401:
        description: Unauthorized, such as token validation failure.
      500:
        description: Internal server error.
    """
    logger.info("Retrieving user details")
    # Your logic here to decode the token, extract user ID, and fetch user details

    return handle_user_details(current_user_id)
            
    
