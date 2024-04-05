from functools import wraps
from time import time

from flask import abort, g, request
from loguru import logger


def rate_limit(max_requests, time_window):
    """Rate limiter decorator with default values that can be overridden.

    Args:
        max_requests (int, optional): The maximum amount of requests allowed. Defaults to 100.
        time_window (int, optional): The time window in seconds which the max requests is applied to. Defaults to 60.
    """

    def decorator(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            # Initialize g.rate_limit if it doesn't exist
            if not hasattr(g, 'rate_limit'):
                g.rate_limit = {}
            # Create a unique key for each endpoint and IP
            key = f"rate_limit:{request.endpoint}:{request.remote_addr}"
            if key not in g:
                g.rate_limit[key] = (0, time())

            requests, last_checked = g.rate_limit[key]

            # Reset the count if time window has passed
            if time() - last_checked > time_window:
                g.rate_limit[key] = (1, time())
            elif requests >= max_requests:
                abort(429, "Too many requests.")
            else:
                g.rate_limit[key] = (requests + 1, last_checked)

            logger.info(f"Within rate limit for {request.endpoint}")
            return f(*args, **kwargs)

        return wrapped

    return decorator
