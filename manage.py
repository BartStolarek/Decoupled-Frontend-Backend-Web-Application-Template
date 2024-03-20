#!/usr/bin/env python
# Standard Imports
import glob
import json
import os
import subprocess

# Third Party Imports
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell

# Local Imports
from server import create_server, db
from server.config import Config
from server.models import Role, User

app = create_server(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

####################################################################################
#
#         Project Formatting Functions
#
####################################################################################


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py server/'
    yapf = 'yapf -r -i *.py server/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


####################################################################################
#
#         Setup Functions
#
####################################################################################


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


@manager.command
def setup_prod():
    """Runs the set-up needed for production."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    Role.insert_roles()
    admin_query = Role.query.filter_by(name='Administrator')
    if admin_query.first() is not None:
        if User.query.filter_by(email=Config.ADMIN_EMAIL).first() is None:
            user = User(first_name='Admin',
                        last_name='Account',
                        password=Config.ADMIN_PASSWORD,
                        confirmed=True,
                        email=Config.ADMIN_EMAIL)
            db.session.add(user)
            db.session.commit()
            print('Added administrator {}'.format(user.full_name()))
    user_query = Role.query.filter_by(name='User')
    if user_query.first() is not None:
        if User.query.filter_by(email=Config.FAKE_EMAIL).first() is None:
            user = User(first_name=Config.FLASK_CONFIG,
                        last_name='Fake',
                        password=Config.FAKE_PASSWORD,
                        confirmed=True,
                        email=Config.FAKE_EMAIL)
            db.session.add(user)
            db.session.commit()
            print('Added Fake User {}'.format(user.full_name()))


####################################################################################
#
#         Database Operations
#
####################################################################################


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    response = input(
        "Are you sure you want to drop all data, perhaps migrate is better? (y/n): "
    )
    if response.lower() == 'y':
        db.drop_all()
        db.create_all()
        db.session.commit()


@manager.command
def add_new_tables_db():
    """
    Adds new tables to the database.
    """
    db.create_all()
    db.session.commit()


@manager.command
def drop_table(tablename):
    """
    Drop a specific table from the database.
    """
    db.drop_table(tablename)
    db.session.commit()


@manager.option('-n',
                '--number-users',
                default=10,
                type=int,
                help='Number of each model type to create',
                dest='number_users')
def add_fake_data(number_users):
    """
    Adds fake data to the database.
    """
    User.generate_fake(count=number_users)


@manager.option('-e',
                '--email',
                dest='email',
                help='The user email to be updated')
@manager.option('--first_name',
                dest='first_name',
                help='The first name to be set')
@manager.option('--last_name',
                dest='last_name',
                help='The last name to be set')
@manager.option('--password', dest='password', help='The password to be set')
@manager.option('--role_id',
                dest='role_id',
                default=1,
                help='The role_id to be set')
def register_user(email, first_name, last_name, password, role_id,
                  arb_email_alerts, posEV_email_alerts):

    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            return

        user = User(first_name=first_name,
                    last_name=last_name,
                    password=password,
                    confirmed=True,
                    email=email,
                    role_id=int(role_id))
        db.session.add(user)
        db.session.commit()


@manager.option('-e',
                '--email',
                dest='email',
                help='The user email to be updated')
def delete_user(email):

    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if not user:
            return

        db.session.delete(user)
        db.session.commit()


@manager.option('-e',
                '--email',
                dest='email',
                help='The user email to be updated')
@manager.option('-a',
                '--attribute',
                dest='attribute',
                help='The attribute to be updated')
@manager.option('-v', '--value', dest='value', help='The value to be set')
def update_user(email, attribute, value):

    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if not user:
            return
        if attribute == 'password':
            user_input = input(
                "Changing the password might not include the password hash, check it was applied. Otherwise delete user and create a new one. Continue (y/n)?"
            )
            if user_input == 'n':
                return
        attribute_type = type(getattr(user, attribute))

        try:
            if attribute_type == bool:
                if 'false' in value.lower():
                    value = False
                elif 'true' in value.lower():
                    value = True
                else:
                    raise ValueError(
                        f"Value '{value}' is not a valid boolean value")
            elif attribute_type == int:
                value = int(value)
            elif attribute_type == float:
                value = float(value)
            elif attribute_type == str:
                value = str(value)
            elif attribute_type == list:
                value = value.strip("[]").replace(" ", "").split(",")
            elif attribute_type == dict:
                value = json.loads(value)
        except Exception as e:
            return

        setattr(user, attribute, value)
        db.session.merge(user)
        db.session.commit()


####################################################################################
#
#         Unit Testing
#
####################################################################################


@manager.option('-f',
                '--filename',
                dest='filename',
                default=None,
                help='The file name to be tested')
@manager.option('-c',
                '--coverage',
                dest='coverage_console',
                default=False,
                help='Whether to run coverage or not')
def test(filename=None, coverage_console=False):
    """Run the unit tests."""
    # Define the base directory for tests
    base_test_dir = os.path.abspath("tests/")

    if filename:
        # Search for the file within the base_test_dir
        test_path = next(
            (os.path.join(base_test_dir, f)
             for f in glob.iglob(f"**/{filename}.py", recursive=True)), None)
        if not test_path:
            print(f"Test file {filename}.py not found in {base_test_dir}!")
            return 1
    else:
        test_path = base_test_dir

    # Check if the data/tests directory exists, if not, create it
    if not os.path.exists('data/tests'):
        os.makedirs('data/tests')

    # Delete .coverage file before running coverage report
    if os.path.exists('.coverage'):
        os.remove('.coverage')

    # Run pytest with coverage
    cmd = f"coverage run -m pytest {test_path}"
    exit_code = os.system(cmd)

    # Generate the coverage report
    if coverage_console:
        os.system("coverage report -m")
    os.system("coverage html -d data/tests/htmlcov")

    print("Coverage report generated at: data/tests/htmlcov/index.html")

    return exit_code


####################################################################################
#
#         Global
#
####################################################################################


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
port = int(os.getenv('PORT', 5000))
manager.add_command('runserver', Server(host="0.0.0.0", port=port))

if __name__ == '__main__':
    manager.run()
