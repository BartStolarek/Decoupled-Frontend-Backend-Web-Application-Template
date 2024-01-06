import pytest
from app import create_app, db
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='function')
def test_client():
    # Configure your app for testing
    app = create_app('unittesting')
    app.config['TESTING'] = True
    app_context = app.app_context()
    app_context.push()

    # Connect to the server
    # Use the SQLALCHEMY_DATABASE_URI from the app's configuration
    DATABASE_URL = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(DATABASE_URL)

    # Create a new test database and tables
    if not database_exists(engine.url):
        create_database(engine.url)
    db.create_all()

    # Create a new Session bound to the test engine
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # this is the session object that will be used for the tests

    # Cleanup: Close the session, drop the test database, and close all connections
    session.close()
    db.drop_all()
    drop_database(engine.url)
    engine.dispose()
    app_context.pop()

def test_app_exists(test_client):
    assert current_app is not None

def test_app_is_testing(test_client):
    assert current_app.config['TESTING']
