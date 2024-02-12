from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

from server.extensions import db
from server.models.user import User


def register_user(user_dict: dict) -> tuple[bool, str]:
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
            date_of_birth=user_dict.get("date_of_birth"),
            height_cm=user_dict.get("height"),
            weight_kg=user_dict.get("weight"),
            gender=user_dict.get("gender"),
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


def delete_user(user_dict: dict) -> tuple[bool, str]:
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


def update_user(user_dict: dict) -> tuple[bool, str]:
    """Update a user in the database.

    Args:
        user_dict (dict): A dict of user data to be used to update a user in the database.

    Returns:
        bool: whether or not the user was successfully updated.
        str: a message indicating the result of the update.
    """
    try:
        # Check if user exists
        user_email = user_dict.get('email')
        existing_user = User.query.filter_by(email=user_email).first()
        if existing_user is None:
            return False, 'User does not exist'

        # Update the email if new_email is provided
        if 'new_email' in user_dict:
            user_dict['email'] = user_dict.pop('new_email')

        # Create a new User instance with updated data
        updated_user = User(**user_dict)

        # Merge the new instance with the existing one in the session
        db.session.merge(updated_user)
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



def get_users(search_column: str, search_value: str) -> list[User]:
    """Get a list of users that match search parameter

    Args:
        search_column (str): The column to search for the user
        search_value (str): The value to search for in the column

    Returns:
        list[User]: list of users that were found matching those search parameters
    """
    try:
        return User.query.filter(text(f"{search_column}=:value")).params(value=search_value).all()
    except Exception as e:
        logger.error(f"Unexpected Error trying to find users: {e}")
        return []

    
def get_user_details(user_id: int) -> tuple[bool, str, dict]:
    """Get user details from the database. This function obtains the details dynamically. 

    Args:
        user_id (int): The unique id of the user being retrieved

    Returns:
        bool: whether or not the user was successfully retrieved
        str: a message indicating the result of the retrieval
        dict: a dict containing the user's details
    """
    try:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return False, 'User does not exist', {}
        
        user_dict = user.to_dict()
        
        return True, "Success", user_dict
    except Exception as e:
        logger.error(f"Unexpected Error trying to find user: {e}")
        return False, 'Unexpected error occurred', {}
