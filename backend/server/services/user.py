from loguru import logger
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from server.extensions import db
from server.models.user import User


def create_user(user_dict: dict) -> tuple[bool, str]:
    """Create a new user in the database

    Args:
        user_dict (dict): A dict of user data to be used to create a new user in the database

    Returns:
        bool: whether or not the user was successfully created
        str: a message indicating the result of the creation
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
        return True, 'User created successfully'

    except IntegrityError as e:
        logger.error(f"Integrity Error: {e}")
        db.session.rollback()
        error_info = str(e.orig)
        if 'UNIQUE constraint failed: users.email' in error_info:
            return False, 'Integrity Error: User with that email already exists'
        return False, 'Integrity Error: Could not create user'

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occured. Could not create user'


def get_users() -> tuple[bool, str, list[User]]:
    """Get all users from the database

    Returns:
        bool: whether or not the users were successfully retrieved
        str: a message indicating the result of the retrieval
        list[User]: a list of users
    """
    try:
        users = User.query.all()
        return True, 'Success', users
    except Exception as e:
        logger.error(f"Unexpected Error trying to find users: {e}")
        return False, 'Unexpected error occurred', []

def get_user_by_id(user_id: int) -> tuple[bool, str, User]:
    """Get a user by their unique id

    Args:
        user_id (int): The unique id of the user being retrieved

    Returns:
        bool: whether or not the user was successfully retrieved
        str: a message indicating the result of the retrieval
        User: a user object
    """
    try:
        user = User.query.filter_by(id=user_id).first()
        return True, 'Success', user
    except Exception as e:
        logger.error(f"Unexpected Error trying to find user: {e}")
        return False, 'Unexpected error occurred', {}
    

def update_user(user: User, user_dict: dict) -> tuple[bool, str, User]:
    """Update a user in the database

    Args:
        user (User): The user object to be updated
        user_dict (dict): A dict of user data to be used to update the user in the database

    Returns:
        bool: whether or not the user was successfully updated
        str: a message indicating the result of the update
        User: the updated user object
    """
    try:
        # Update the user with the new data
        for key, value in user_dict.items():
            setattr(user, key, value)

        # Commit the changes to the database
        db.session.commit()

        logger.info(f"User {user.email} updated in database")
        return True, 'User updated successfully', user

    except IntegrityError as e:
        logger.error(f"Integrity Error: {e}")
        db.session.rollback()
        error_info = str(e.orig)
        if 'UNIQUE constraint failed: users.email' in error_info:
            return False, 'Integrity Error: User with that email already exists', {}
        return False, 'Integrity Error: Could not update user', {}

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occurred. Could not update user', {}
    
def update_user_by_id(user_id: int, user_dict: dict) -> tuple[bool, str, User]:
    """Update a user in the database by their unique id

    Args:
        user_id (int): The unique id of the user being updated
        user_dict (dict): A dict of user data to be used to update the user in the database

    Returns:
        bool: whether or not the user was successfully updated
        str: a message indicating the result of the update
        User: the updated user object
    """
    try:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return False, 'User does not exist', {}

        # Update the user with the new data
        for key, value in user_dict.items():
            setattr(user, key, value)

        # Commit the changes to the database
        db.session.commit()

        logger.info(f"User {user.email} updated in database")
        return True, 'User updated successfully', user

    except IntegrityError as e:
        logger.error(f"Integrity Error: {e}")
        db.session.rollback()
        error_info = str(e.orig)
        if 'UNIQUE constraint failed: users.email' in error_info:
            return False, 'Integrity Error: User with that email already exists', {}
        return False, 'Integrity Error: Could not update user', {}

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occurred. Could not update user', {}


def delete_user(user: User) -> tuple[bool, str]:
    """Delete a user from the database

    Args:
        user (User): The user object to be deleted

    Returns:
        bool: whether or not the user was successfully deleted
        str: a message indicating the result of the deletion
    """
    try:
        db.session.delete(user)
        db.session.commit()

        logger.info(f"User {user.email} deleted from database")
        return True, 'User deleted successfully'

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occurred. Could not delete user'
    
    
def delete_user_by_id(user_id: int) -> tuple[bool, str]:
    """Delete a user from the database by their unique id

    Args:
        user_id (int): The unique id of the user being deleted

    Returns:
        bool: whether or not the user was successfully deleted
        str: a message indicating the result of the deletion
    """
    try:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return False, 'User does not exist'

        db.session.delete(user)
        db.session.commit()

        logger.info(f"User {user.email} deleted from database")
        return True, 'User deleted successfully'

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        db.session.rollback()
        return False, 'Unexpected error occurred. Could not delete user'

