from server.models.user import User
from loguru import logger
from server import db
from sqlalchemy.exc import IntegrityError


def register_user(user_dict: dict):
    """Register a new user

    Args:
        user_data (dict): A dict of user data to be used to create a new user in the database

    Returns:
        bool: whether or not the user was successfully registered
        str: a message indicating the result of the registration
    """
    try:
        user = User(
            first_name=user_dict.get("first_name"),
            last_name=user_dict.get("last_name"),
            email=user_dict.get("email"),
            # Set the password using the password setter
        )
        user.password = user_dict.get("password")

        # Add the user to the session and commit
        db.session.add(user)
        db.session.commit()

        logger.info(f"User {user.email} saved to database")
        return True, 'User registered successfully'
    
    except IntegrityError as e:
        logger.error(f"Integrity Error: {e}")
        db.session.rollback()
        error_info = str(e.orig)
        if 'UNIQUE constraint failed: users.email' in error_info:
            return False, 'Integrity Error: User with that email already exists'
        return False, 'Integrity Error: Could not register user'
    
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occured. Could not register user'


def delete_user(user_dict: dict):
    """Delete a user from the database

    Args:
        user_email (str): The unique email address of the user being deleted

    Returns:
        bool: whether or not the user was successfully deleted
        str: a message indicating the result of the deletion
    """
    try:
        user_email = user_dict.get('email')
        user = User.query.filter_by(email=user_email).first()
        if user is None:
            return False, 'User does not exist'
        db.session.delete(user)
        db.session.commit()
        logger.info(f"User {user_email} deleted from database")
        return True, 'User deleted successfully'
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occured. Could not delete user'
    

def update_user(user_dict: dict):
    """Update a user in the database

    Args:
        user_data (dict): A dict of user data to be used to update a user in the database

    Returns:
        bool: whether or not the user was successfully updated
        str: a message indicating the result of the update
    """
    try:
        user_email = user_dict.get('email')
        user = User.query.filter_by(email=user_email).first()
        if user is None:
            return False, 'User does not exist'
        
        for key, value in user_dict.items():
            setattr(user, key, value)

        if "new_email" in user_dict:
            user.email = user_dict.get("new_email")
            
        db.session.commit()
        logger.info(f"User {user_email} updated in database")
        return True, 'User updated successfully'
    except IntegrityError as e:
        logger.error(f"Integrity Error: {e}")
        db.session.rollback()
        error_info = str(e.orig)
        if 'UNIQUE constraint failed: users.email' in error_info:
            return False, 'Integrity Error: User with that email already exists'
        return False, 'Integrity Error: Could not update user'
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occurred. Could not update user'
