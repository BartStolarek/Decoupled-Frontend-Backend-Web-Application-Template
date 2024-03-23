from flask import Blueprint, render_template
from loguru import logger

home_blueprint = Blueprint("home", __name__)

# Existing setup code

@home_blueprint.route('/')
def home():
    logger.debug("Rendering home page")
    return render_template('home.html')
