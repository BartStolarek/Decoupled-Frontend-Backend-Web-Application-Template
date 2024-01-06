HTTP_STATUS_CODES = {
    # 1xx: Informational
    100: {"status": "informational", "message": "Continue"},
    101: {"status": "informational", "message": "Switching Protocols"},
    102: {"status": "informational", "message": "Processing"},

    # 2xx: Success
    200: {"status": "success", "message": "OK"},
    201: {"status": "success", "message": "Created"},
    202: {"status": "success", "message": "Accepted"},
    203: {"status": "success", "message": "Non-Authoritative Information"},
    204: {"status": "success", "message": "No Content"},
    205: {"status": "success", "message": "Reset Content"},
    206: {"status": "success", "message": "Partial Content"},
    207: {"status": "success", "message": "Multi-Status"},
    208: {"status": "success", "message": "Already Reported"},
    226: {"status": "success", "message": "IM Used"},

    # 3xx: Redirection
    300: {"status": "redirection", "message": "Multiple Choices"},
    301: {"status": "redirection", "message": "Moved Permanently"},
    302: {"status": "redirection", "message": "Found"},
    303: {"status": "redirection", "message": "See Other"},
    304: {"status": "redirection", "message": "Not Modified"},
    305: {"status": "redirection", "message": "Use Proxy"},
    307: {"status": "redirection", "message": "Temporary Redirect"},
    308: {"status": "redirection", "message": "Permanent Redirect"},

    # 4xx: Client Error
    400: {"status": "client error", "message": "Bad Request"},
    401: {"status": "client error", "message": "Unauthorized"},
    402: {"status": "client error", "message": "Payment Required"},
    403: {"status": "client error", "message": "Forbidden"},
    404: {"status": "client error", "message": "Not Found"},
    405: {"status": "client error", "message": "Method Not Allowed"},
    406: {"status": "client error", "message": "Not Acceptable"},
    407: {"status": "client error", "message": "Proxy Authentication Required"},
    408: {"status": "client error", "message": "Request Timeout"},
    409: {"status": "client error", "message": "Conflict"},
    410: {"status": "client error", "message": "Gone"},
    411: {"status": "client error", "message": "Length Required"},
    412: {"status": "client error", "message": "Precondition Failed"},
    413: {"status": "client error", "message": "Payload Too Large"},
    414: {"status": "client error", "message": "URI Too Long"},
    415: {"status": "client error", "message": "Unsupported Media Type"},
    416: {"status": "client error", "message": "Range Not Satisfiable"},
    417: {"status": "client error", "message": "Expectation Failed"},
    418: {"status": "client error", "message": "I'm a teapot"},  # April Fools' joke
    421: {"status": "client error", "message": "Misdirected Request"},
    422: {"status": "client error", "message": "Unprocessable Entity"},
    423: {"status": "client error", "message": "Locked"},
    424: {"status": "client error", "message": "Failed Dependency"},
    426: {"status": "client error", "message": "Upgrade Required"},
    428: {"status": "client error", "message": "Precondition Required"},
    429: {"status": "client error", "message": "Too Many Requests"},
    431: {"status": "client error", "message": "Request Header Fields Too Large"},
    451: {"status": "client error", "message": "Unavailable For Legal Reasons"},


    # 5xx: Server Error
    500: {"status": "server error", "message": "Internal Server Error"},
    501: {"status": "server error", "message": "Not Implemented"},
    502: {"status": "server error", "message": "Bad Gateway"},
    503: {"status": "server error", "message": "Service Unavailable"},
    504: {"status": "server error", "message": "Gateway Timeout"},
    505: {"status": "server error", "message": "HTTP Version Not Supported"},
    506: {"status": "server error", "message": "Variant Also Negotiates"},
    507: {"status": "server error", "message": "Insufficient Storage"},
    508: {"status": "server error", "message": "Loop Detected"},
    510: {"status": "server error", "message": "Not Extended"},
    511: {"status": "server error", "message": "Network Authentication Required"},

}
