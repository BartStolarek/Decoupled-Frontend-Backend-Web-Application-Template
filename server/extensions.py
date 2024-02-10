from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_compress import Compress
from flask_rq import RQ

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
compress = Compress()
