from server.models.user import User
from loguru import logger
from server import db

def register_user(user_data):
    user = User(
        first_name=user_data.get("first_name"),
        last_name=user_data.get("last_name"),
        email=user_data.get("email"),
        # Set the password using the password setter
    )
    user.password = user_data.get("password")

    # Add the user to the session and commit
    db.session.add(user)
    db.session.commit()

    logger.info(f"User {user.email} saved to database")
    return True, 'User registered successfully'
