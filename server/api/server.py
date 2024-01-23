from flask import Blueprint, Response, jsonify

server_blueprint = Blueprint('server', __name__)


@server_blueprint.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to ensure the server is running.
    """
    print("print in server health check")
    return jsonify({
        "status_code": 418,
        # "data": Add in data here if necessary
    })
