import jwt
import datetime
from flask import Blueprint, request, jsonify
from server.models import User  # Your User model
from server.schema import UserSchema  # Your User schema
from server.services import user_service  # Your user service
from server.handler import rate_limit
from werkzeug.security import check_password_hash

# Assuming you have a SECRET_KEY defined in your config
from flask import current_app

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def register():
    """
    Register a new user.
    """
    user_schema = UserSchema()
    errors = user_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400

    success, message = user_service.register_user(request.json)
    
    return jsonify({"status": "ok" if success else "error", "message": message}), 200 if success else 400



@user_blueprint.route('/authorize', methods=['POST'])
@rate_limit(50, 30)  # Applying custom rate limit as decorator
def authorize():
    """
    Authorize a user and return a JWT.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        # Generate JWT token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({'token': token.decode('UTF-8')}), 200

    return jsonify({'error': 'Invalid credentials'}), 401