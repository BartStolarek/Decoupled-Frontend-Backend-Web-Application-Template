from flask import jsonify
from loguru import logger

HTTP_STATUS_CODES = {
    # 1xx: Informational
    100: {
        "status": "informational",
        "message": "Continue"
    },
    101: {
        "status": "informational",
        "message": "Switching Protocols"
    },
    102: {
        "status": "informational",
        "message": "Processing"
    },

    # 2xx: Success
    200: {
        "status": "success",
        "message": "OK"
    },
    201: {
        "status": "success",
        "message": "Created"
    },
    202: {
        "status": "success",
        "message": "Accepted"
    },
    203: {
        "status": "success",
        "message": "Non-Authoritative Information"
    },
    204: {
        "status": "success",
        "message": "No Content"
    },
    205: {
        "status": "success",
        "message": "Reset Content"
    },
    206: {
        "status": "success",
        "message": "Partial Content"
    },
    207: {
        "status": "success",
        "message": "Multi-Status"
    },
    208: {
        "status": "success",
        "message": "Already Reported"
    },
    226: {
        "status": "success",
        "message": "IM Used"
    },

    # 3xx: Redirection
    300: {
        "status": "redirection",
        "message": "Multiple Choices"
    },
    301: {
        "status": "redirection",
        "message": "Moved Permanently"
    },
    302: {
        "status": "redirection",
        "message": "Found"
    },
    303: {
        "status": "redirection",
        "message": "See Other"
    },
    304: {
        "status": "redirection",
        "message": "Not Modified"
    },
    305: {
        "status": "redirection",
        "message": "Use Proxy"
    },
    307: {
        "status": "redirection",
        "message": "Temporary Redirect"
    },
    308: {
        "status": "redirection",
        "message": "Permanent Redirect"
    },

    # 4xx: Client Error
    400: {
        "status": "Client Error",
        "message": "Bad Request"
    },
    401: {
        "status": "Client Error",
        "message": "Unauthorized"
    },
    402: {
        "status": "Client Error",
        "message": "Payment Required"
    },
    403: {
        "status": "Client Error",
        "message": "Forbidden"
    },
    404: {
        "status": "Client Error",
        "message": "API Endpoint Not Found"
    },
    405: {
        "status": "Client Error",
        "message": "Method Not Allowed"
    },
    406: {
        "status": "Client Error",
        "message": "Not Acceptable"
    },
    407: {
        "status": "Client Error",
        "message": "Proxy Authentication Required"
    },
    408: {
        "status": "Client Error",
        "message": "Request Timeout"
    },
    409: {
        "status": "Client Error",
        "message": "Conflict"
    },
    410: {
        "status": "Client Error",
        "message": "Gone"
    },
    411: {
        "status": "Client Error",
        "message": "Length Required"
    },
    412: {
        "status": "Client Error",
        "message": "Precondition Failed"
    },
    413: {
        "status": "Client Error",
        "message": "Payload Too Large"
    },
    414: {
        "status": "Client Error",
        "message": "URI Too Long"
    },
    415: {
        "status": "Client Error",
        "message": "Unsupported Media Type"
    },
    416: {
        "status": "Client Error",
        "message": "Range Not Satisfiable"
    },
    417: {
        "status": "Client Error",
        "message": "Expectation Failed"
    },
    418: {
        "status": "Client Error",
        "message": "I'm a teapot"
    },  # April Fools' joke
    421: {
        "status": "Client Error",
        "message": "Misdirected Request"
    },
    422: {
        "status": "Client Error",
        "message": "Unprocessable Entity"
    },
    423: {
        "status": "Client Error",
        "message": "Locked"
    },
    424: {
        "status": "Client Error",
        "message": "Failed Dependency"
    },
    426: {
        "status": "Client Error",
        "message": "Upgrade Required"
    },
    428: {
        "status": "Client Error",
        "message": "Precondition Required"
    },
    429: {
        "status": "Client Error",
        "message": "Too Many Requests"
    },
    431: {
        "status": "Client Error",
        "message": "Request Header Fields Too Large"
    },
    451: {
        "status": "Client Error",
        "message": "Unavailable For Legal Reasons"
    },

    # 5xx: Server Error
    500: {
        "status": "server error",
        "message": "Internal Server Error"
    },
    501: {
        "status": "server error",
        "message": "Not Implemented"
    },
    502: {
        "status": "server error",
        "message": "Bad Gateway"
    },
    503: {
        "status": "server error",
        "message": "Service Unavailable"
    },
    504: {
        "status": "server error",
        "message": "Gateway Timeout"
    },
    505: {
        "status": "server error",
        "message": "HTTP Version Not Supported"
    },
    506: {
        "status": "server error",
        "message": "Variant Also Negotiates"
    },
    507: {
        "status": "server error",
        "message": "Insufficient Storage"
    },
    508: {
        "status": "server error",
        "message": "Loop Detected"
    },
    510: {
        "status": "server error",
        "message": "Not Extended"
    },
    511: {
        "status": "server error",
        "message": "Network Authentication Required"
    },
}


def handle_status_code(code: int, data: dict = None) -> jsonify:
    """Return a response object with the appropriate status code and message

    Args:
        code (int): The HTTP status code
        data (dict, optional): A dict of additional information. Defaults to None.

    Returns:
        json: A json response object
    """
    status_info = HTTP_STATUS_CODES.get(code, {
        "status": "error",
        "message": "Unknown error"
    })

    # Initialize the response dictionary
    response_dict = {
        "status_code": code,
        "message": status_info["message"],
        "status": status_info["status"]
    }

    # Add data to the response dictionary if provided
    if data is not None and isinstance(data, dict):
        response_dict["data"] = data
    elif data is not None and not isinstance(data, dict):
        code = 500
        logger.error(
            f'{code} API Error: data provided must be a dictionary or None')
        # Update status_info for the new code
        status_info = HTTP_STATUS_CODES.get(code, {
            "status": "error",
            "message": "Unknown error"
        })
        response_dict.update({
            "status_code": code,
            "message": status_info["message"],
            "status": status_info["status"]
        })

    # Log the message based on the status code
    if 400 <= code <= 599:
        logger.error(f'{code} API Error: {status_info["message"]}')
    else:
        logger.info(f'{code} API Status: {status_info["message"]}')

    response = jsonify(response_dict)
    response.status_code = code  # Set the correct status code
    return response
