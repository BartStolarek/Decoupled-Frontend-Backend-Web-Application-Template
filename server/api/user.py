from datetime import datetime, timedelta
from loguru import logger

import jwt

# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import check_password_hash

from server.handler import rate_limit
from server.models import User  # Your User model
from server.schema import UserSchema  # Your User schema
from server.services import delete_user, register_user, update_user, get_user_details
from server.utils.http_status_codes import handle_status_code
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
    # Function implementation

    user_schema = UserSchema()
    errors = user_schema.validate(request.json)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code
    else:
        user_data = user_schema.load(request.json)
        success, message = register_user(user_data)
        if success:
            logger.info(f"User registered successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            if "Integrity Error: User with that email already exists" in message:
                logger.error(f"User already exists: {message}")
                code = 409
                response = handle_status_code(code, data={"error_info": message})
            else:
                logger.error(f"Internal server error: {message}")
                code = 500
                response = handle_status_code(code, data={"error_info": message})

        return response, code

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
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        logger.error("Authorization failed: Email and password are required")
        code = 400
        response = handle_status_code(code, data={"error_info": "Email and password are required"})
        return response, code

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        try:
            token = jwt.encode(
                {"user_id": user.id, "exp": datetime.utcnow() + timedelta(hours=1)},
                current_app.config["SECRET_KEY"],
                algorithm="HS256",
            )
            logger.info(f"User {email} authorized successfully")
            code = 200
            response = handle_status_code(code, data={"user_token": token})
            return response, code
        except Exception as e:
            logger.error(f"JWT encoding failed: {str(e)}")
            code = 500
            response = handle_status_code(code, data={"error_info": "Internal server error during JWT encoding"})
            return response, code
    else:
        logger.warning(f"Authorization failed for user {email}: Invalid credentials")
        code = 401
        response = handle_status_code(code, data={"error_info": "Invalid credentials"})
        return response, code


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
    user_schema = UserSchema(only=["email"])
    errors = user_schema.validate(request.json)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code
    else:
        user_data = user_schema.load(request.json)
        success, message = delete_user(user_data)
        if success:
            logger.info(f"User deleted successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            logger.error(f"Conflict error: {message}")
            code = 409
            response = handle_status_code(code, data={"error_info": message})
        return response, code


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
    user_schema = UserSchema(partial=True)
    errors = user_schema.validate(request.json)
    if errors:
        logger.error(f"Failed to validate user against user schema: {errors}")
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code
    else:
        user_data = user_schema.load(request.json)
        success, message = update_user(user_data)
        if success:
            logger.info(f"User updated successfully: {message}")
            code = 201
            response = handle_status_code(code, data={"info": message})
        else:
            if "Integrity Error: User with that email already exists" in message:
                logger.error(f"User already exists: {message}")
                code = 409
                response = handle_status_code(code, data={"error_info": message})
            else:
                logger.error(f"Internal server error: {message}")
                code = 500
                response = handle_status_code(code, data={"error_info": message})

        return response, code


@user_blueprint.route("/user-details", methods=["GET"])
@token_required
@rate_limit(50, 30)
def user_details(current_user_id):
    """
    Retrieve the details of the currently logged-in user.
    ---
    tags:
        - user
    description: Retrieves details of the currently logged-in user based on their user ID.
    parameters:
      - in: header
        name: Authorization
        description: Access token to authenticate the request.
        required: true
        schema:
          type: string
      - in: path
        name: current_user_id
        description: The ID of the current user whose details are being requested.
        required: true
        schema:
          type: integer
    responses:
      200:
        description: User details retrieved successfully. Returns user details.
        content:
      400:
        description: Bad request or user does not exist.
      500:
        description: Internal server error.
    """
    try:
        success, message, user_details = get_user_details(current_user_id)
        if success:
            code = 200
            response = handle_status_code(code, data={"user_details": user_details})
            logger.info(f"User details retrieved successfully: {message}. {user_details}")
        else:
            if message == "User does not exist":
                code = 400
                response = handle_status_code(code, data={"error_info": message})
                logger.error(f"User does not exist: {message}")
            else:
                code = 500
                response = handle_status_code(code, data={"error_info": message})
                logger.error(f"Internal server error: {message}")
    except Exception as e:
        logger.error(f"User details retrieval failed: {str(e)}")
        code = 500
        response = handle_status_code(code, data={"error_info": "Internal server error"})
        
    return response, code
            
    
