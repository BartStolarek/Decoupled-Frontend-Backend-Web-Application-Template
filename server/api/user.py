import datetime

import jwt
# Assuming you have a SECRET_KEY defined in your config
from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import check_password_hash

from server.handler import rate_limit
from server.models import User  # Your User model
from server.schema import UserSchema  # Your User schema
from server.services import delete_user, register_user, update_user
from server.utils.http_status_codes import handle_status_code

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register', methods=['POST'])
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
            - email
            - password
          properties:
            first_name:
              type: string
              description: First name of the user
            last_name:
              type: string
              description: Last name of the user
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
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code

    success, message = register_user(request.json)
    if success:
        code = 201
        response = handle_status_code(code, data={"info": message})
    else:
        if 'Integrity Error: User with that email already exists' in message:
            code = 409
            response = handle_status_code(code, data={"error_info": message})
        else:
            code = 500
            response = handle_status_code(code, data={"error_info": message})

    return response, code


@user_blueprint.route('/delete', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
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
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code

    success, message = delete_user(request.json)
    if success:
        code = 201
        response = handle_status_code(code, data={"info": message})
    else:
        code = 409
        response = handle_status_code(code, data={"error_info": message})
    return response, code


@user_blueprint.route('/update', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
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
        code = 400
        response = handle_status_code(code, data={"error_info": errors})
        return response, code

    success, message = update_user(request.json)
    if success:
        code = 201
        response = handle_status_code(code, data={"info": message})
    else:
        if 'Integrity Error: User with that email already exists' in message:
            code = 409
            response = handle_status_code(code, data={"error_info": message})
        else:
            code = 500
            response = handle_status_code(code, data={"error_info": message})

    return response, code


@user_blueprint.route('/authorize', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def authorize():
    """
    NOT IMPLEMENTED - Authorize a user and return a JWT token.
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
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        # Generate JWT token
        token = jwt.encode(
            {
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

        return jsonify({'token': token.decode('UTF-8')}), 200

    return jsonify({'error': 'Invalid credentials'}), 401
