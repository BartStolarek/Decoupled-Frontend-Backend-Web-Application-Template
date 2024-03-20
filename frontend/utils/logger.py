# Standard Imports
import os
import sys

# Third Party Imports
from loguru import logger

# Local Imports
from frontend.config import FrontEndConfig, root_project_dir


def setup_logger():

    # Obtain logger details from config
    environment = os.getenv("FLASK_CONFIG", "production")
    diagnose = False if environment == "production" else True
    logging_level = os.getenv("LOGGING_LEVEL", "INFO")

    # Remove the default handler
    logger.remove()

    # Configure Loguru logger
    logger_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>")
    logger.add(sys.stderr,
               colorize=True,
               diagnose=diagnose,
               format=logger_format,
               level=logging_level)

    # Check if directory exists
    if not os.path.exists(f"{root_project_dir}/data/frontend/logs"):
        os.makedirs(f"{root_project_dir}/data/frontend/logs")

    # Add a log file
    logger.add(
        f"{root_project_dir}/data/frontend/logs/frontend.log",
        diagnose=diagnose,
        retention="10 days",
        enqueue=True,
        #compression="zip",
        format=logger_format,
        level="INFO")
