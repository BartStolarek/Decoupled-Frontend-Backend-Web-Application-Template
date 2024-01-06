from flask import request, abort

def authenticate():
    if request.endpoint in ['user.register']:  # Skip authentication for user registration
        return
    # Add your authentication logic here
    token = request.headers.get('Authorization')
    if not token or not valid_token(token):
        abort(401, "Unauthorized")
