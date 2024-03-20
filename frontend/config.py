import os
import sys

serverdir = os.path.abspath(os.path.dirname(__file__))

check_dir = serverdir
while not os.path.exists(os.path.join(check_dir, 'server')):
    check_dir = os.path.dirname(check_dir)
root_project_dir = check_dir

# Look for config.env on the same level as config.py
config_env_path = os.path.join(serverdir, 'config.env')
if os.path.exists(config_env_path):
    print('Importing environment from .env file')
    for line in open(config_env_path):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")
else:
    print(
        'config.env file not found, please read README.md for config.env file structure'
    )


class FrontEndConfig:
    APP_NAME = os.environ.get('APP_NAME', 'Flask API Boilerplate')
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

    # Flask Config
    FLASK_CONFIG = os.environ.get('FLASK_CONFIG', 'default')

    # SQLAlchemy Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Log Level
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

    # Admin and Fake user
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'noemail@domain.com')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
    FAKE_EMAIL = os.environ.get('FAKE_EMAIL')
    FAKE_PASSWORD = os.environ.get('FAKE_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(FrontEndConfig):
    ENV = 'development'
    DEBUG = True
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL',
        'sqlite:///' + os.path.join(root_project_dir, 'data-dev.sqlite'))

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class TestingConfig(FrontEndConfig):
    ENV = 'testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL',
        'sqlite:///' + os.path.join(root_project_dir, 'data-test.sqlite'))

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN TESTING MODE.  \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class UnitTestingConfig(FrontEndConfig):
    ENV = 'unittesting'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'UNITTEST_DATABASE_URL',
        'sqlite:///' + os.path.join(root_project_dir, 'data-unittest.sqlite'))
    WTF_CSRF_ENABLED = False

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN UNIT TESTING MODE. \
              YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class ProductionConfig(FrontEndConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(root_project_dir, 'data.sqlite'))

    @classmethod
    def init_app(cls, app):
        FrontEndConfig.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET KEY IS NOT SET!'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'unittesting': UnitTestingConfig,
    'default': DevelopmentConfig
}
