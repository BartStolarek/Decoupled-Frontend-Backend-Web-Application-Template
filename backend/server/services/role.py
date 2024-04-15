from loguru import logger
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from server.extensions import db
from server.models import Role


def get_roles() -> tuple[bool, str, list[Role]]:
    try:
        roles = Role.query.all()
        return True, 'Success', roles
    except Exception as e:
        logger.error(f"Unexpected Error trying to find roles: {e}")
        return False, 'Unexpected error occurred', []
