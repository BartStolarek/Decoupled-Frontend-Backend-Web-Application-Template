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
    @user_blueprint.route('/register', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def register():
    """
    
    Registers a new user with the provided first name, last name, email, and password.
    
    - **URL**: `/user/register`
    - **Method**: `POST`
    - **Payload**:
        - `first_name`: User's first name (required)
        - `last_name`: User's last name (required)
        - `email`: User's email address (required)
        - `password`: User's password (required)
    - **Success Response**:
        - **Code**: 201 CREATED
        - **Content**: `{ "info": "User registered successfully" }`
    - **Error Response**:
        - **Code**: 400 BAD REQUEST
        - **Content**: `{ "error_info": "<validation error message>" }`
          - Occurs if the payload data does not pass the schema validation.
        - **Code**: 409 CONFLICT
        - **Content**: `{ "error_info": "<Integrity error message>" }`
          - Occurs if there is an integrity error, such as a duplicate email.
        - **Code**: 500 INTERNAL SERVER ERROR
        - **Content**: `{ "error_info": "<server error message>" }`
          - Indicates a server error.
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
    
    - **URL**: `/user/delete`
    - **Method**: `POST`
    - **Payload**:
        - `email`: Email address of the user to be deleted (required)
    - **Success Response**:
        - **Code**: 201 CREATED
        - **Content**: `{ "info": "User deleted successfully" }`
    - **Error Response**:
        - **Code**: 400 BAD REQUEST / 409 CONFLICT
        - **Content**: `{ "error_info": "<error message>" }`
          - Occurs if there is an issue with the payload or user does not exist.
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
    
    - **URL**: `/user/update`
    - **Method**: `POST`
    - **Payload**:
        - User details to update (e.g., `first_name`, `last_name`, `email`). At least one is required.
    - **Success Response**:
        - **Code**: 201 CREATED
        - **Content**: `{ "info": "User updated successfully" }`
    - **Error Response**:
        - **Code**: 400 BAD REQUEST / 409 CONFLICT / 500 INTERNAL SERVER ERROR
        - **Content**: `{ "error_info": "<error message>" }`
          - Occurs if the payload data does not pass the schema validation or user does not exist.
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
    Authorize a user and return a JWT token.
    
    - **URL**: `/user/authorize`
    - **Method**: `POST`
    - **Payload**:
        - `email`: User's email address (required)
        - `password`: User's password (required)
    - **Success Response**:
        - **Code**: 200 OK
        - **Content**: `{ "token": "<JWT token>" }`
    - **Error Response**:
        - **Code**: 400 BAD REQUEST / 401 UNAUTHORIZED
        - **Content**: `{ "error": "Invalid credentials" }`
          - Occurs if email and password are not provided or credentials are incorrect.
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
