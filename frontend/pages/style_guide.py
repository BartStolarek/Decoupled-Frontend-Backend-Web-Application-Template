from flask import Blueprint, render_template
from loguru import logger

style_guide_blueprint = Blueprint("style_guide", __name__)

# Existing setup code

@style_guide_blueprint.route('/styleguide')
def style_guide():
    logger.debug("Rendering style guide page")
    return render_template('style_guide.html')
