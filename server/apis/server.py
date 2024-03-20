from flask import Blueprint, Response, jsonify, send_from_directory
from loguru import logger

from server.utils.http_status_codes import handle_status_code

server_blueprint = Blueprint('server', __name__)


@server_blueprint.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to ensure the server is running.
    """
    logger.info("Health check endpoint hit")
    code = 418
    response = handle_status_code(code, data={"info": "Server is running"})
    return response, code

@server_blueprint.route('/javascript/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/javascript', filename)
