from datetime import datetime, timezone
from loguru import logger


def datetime_to_isoformat_zulu(dt_object) -> str:
    """
    Convert a datetime object to an ISO 8601 formatted string with 'Z' designation for UTC.

    Args:
        dt_object (datetime): The datetime object to convert.

    Returns:
        str: An ISO 8601 formatted string representing the datetime in UTC.
    """
    # Ensure the datetime object is in UTC
    dt_object = dt_object.astimezone(timezone.utc)

    # Convert to ISO format and append 'Z' for UTC designation
    iso_format_str = dt_object.isoformat(timespec='milliseconds').replace(
        '+00:00', 'Z')

    return iso_format_str

def convert_string_to_float(string: str) -> float:
    """
    Convert a string to a float, handling any errors.

    Args:
        string (str): The string to convert to a float.

    Returns:
        float: The float value of the string, or None if the string cannot be converted.
    """
    try:
        return float(string)
    except ValueError:
        logger.error(f"Failed to convert string to float: {string}")
        return string
    
def convert_string_to_int(string: str) -> int:
    """
    Convert a string to an int, handling any errors.

    Args:
        string (str): The string to convert to an int.

    Returns:
        int: The int value of the string, or None if the string cannot be converted.
    """
    try:
        return int(string)
    except ValueError:
        logger.error(f"Failed to convert string to int: {string}")
        return string
    
def convert_string_to_datetime_utc_tz_aware(string: str) -> datetime:
    """
    Convert a string (in format YYYY-MM-DDTHH:MM:SS.%fZ) to a datetime object, handling any errors and ensuring the datetime is timezone-aware.

    Args:
        string (str): The string to convert to a datetime.

    Returns:
        datetime: The datetime object representing the string, or None if the string cannot be converted.
    """
    try:
        dt_object = datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        return dt_object
    except ValueError:
        logger.error(f"Failed to convert string to datetime: {string}")
        return string
    
def convert_datetime_to_string(dt_object: datetime) -> str:
    """
    Convert a datetime object to a string, handling any errors.

    Args:
        dt_object (datetime): The datetime object to convert to a string.

    Returns:
        str: The string value of the datetime, or None if the datetime cannot be converted.
    """
    try:
        return dt_object.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        logger.error(f"Failed to convert datetime to string: {dt_object}")
        return dt_object
