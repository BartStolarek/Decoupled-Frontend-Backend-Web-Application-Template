from flask import Blueprint, render_template
from loguru import logger

login_blueprint = Blueprint("login", __name__)

# Existing setup code

@login_blueprint.route('/login')
def login():
    logger.debug("Rendering login page")
    return render_template('login.html')
