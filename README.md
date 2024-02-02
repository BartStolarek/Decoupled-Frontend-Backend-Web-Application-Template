
# Flask-React Server Template

## Overview

This project is a template for a Python Flask server, designed to expedite the setup of a basic server for serving a web application front end. It incorporates SQLAlchemy for database management and supports multiple environments including development, testing, unit testing, and production. The production environment is the only one configured for non-local (SQLite) databases. The template also integrates seamlessly with React, providing a full-stack solution for web application development.

### Key Features:

- **Database Management:** Utilizes SQLAlchemy.
- **Environments:** Development, Testing, Unit Testing, and Production.
- **Middleware:** Includes an API logger and a response manipulator, enhancing the monitoring and control of API interactions.
- **Logging:** Implemented using Loguru, offering robust logging capabilities.
- **Unit Testing:** Extensive coverage for services, ensuring code reliability and performance.
- **Handlers:** Currently supports rate limiting, ensuring application stability under high load.

### APIs:

**User** <br>
- Register: Allows new users to create an account.
- Delete: Enables users to remove their account.
- Update: Provides functionality for users to update their account details.

To see API documentation, run the server and navigate to 
`http://localhost:5000/apispec_1.json` 
or whatever port you are running the server on.

### How To Use:

This section guides you through setting up and managing your server. Follow the instructions below to get started.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x

## Clone and Initial Setup

To clone and run this project for the first time, follow these steps:
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd [project directory]`
3. Install Python dependencies: `pip install -r requirements.txt`


## Configure

To set up the server, create a `config.env` file in the `server/` directory (not project root directory) with the following variables:

Example config file:
```env
APP_NAME='Flask-React-Boilerplate'
SECRET_KEY=''
FLASK_CONFIG=development
DATABASE_URL=data-dev.sqlite
LOGGING_LEVEL=DEBUG
ADMIN_EMAIL='noemail@domain.com'
ADMIN_PASSWORD='nopassword'
FAKE_EMAIL='user@fake.com'
FAKE_PASSWORD='fakepassword'
```

### Name your app (server)

1. Set the `APP_NAME` variable in `server/config.env` to the name of your app.

    ```env
    APP_NAME='Flask-React-Boilerplate'
    ```

### Generating Secret Key

1. Run the following command in terminal to generate a `SECRET_KEY`:

    ```bash
    $ python3 -c "import secrets; print(secrets.token_hex(16))"
    ```

2. Copy the generated string into your `server/config.env`:

    ```env
    SECRET_KEY=Generated_Random_String
    ```

### Flask Config Environment Variable

1. Set the `FLASK_CONFIG` variable in `server/config.env` to the environment you want to run the server in.

    ```env
    FLASK_CONFIG=development
    ```


Other options include:
| Options (Value)        | Discussion  |
| --------------- | -----|
| `default`   | Default environment, has destinations as development |
| `development` |  Development environment run locally with dev database (sqlite) being stored locally |
| `testing`  | Testing environment run locally with test database (sqlite) being stored locally |
| `unittesting`  | Environment used for unittesting |
| `production`  | Production environment runs locally but connects to deployed (production) database |



### Database Connections variable

1. Set the 'DATABASE_URL' variable in `server/config.env` to the database you want to run the server in.

    ```env
    DATABASE_URL=data-dev.sqlite
    ```

Database instances should be isolated to different environments.

| Options (Value)        | Discussion  |
| --------------- | -----|
| `data-dev.sqlite`   | Development dedicated database stored locally using sqlite |
| `data-test.sqlite` |  Testing dedicated database stored locally using sqlite |
| `data-unittest.sqlite` |  Unit Testing dedicated database stored locally using sqlite |
| postgres URL  | Production dedicated database |

### Logging Level

1. Set the `LOGGING_LEVEL` variable in `server/config.env` to the logging level you want to run the server in.

    ```env
    LOGGING_LEVEL=DEBUG
    ```

Other options include:
| Options (Value)        | Discussion  |
| --------------- | -----|
| `DEBUG`   | Logging useful for debugging, probably best practice to remove these after debugging |
| `INFO` |  Logging useful for a server health check  |
| `WARNING`  | Logging useful to indicate that there may be a issue |
| `ERROR`  | Logging useful to see that error occured by didn't break anything |
| `CRITICAL`  | Logging useful to see that error occured and broke or may cause damage  |


### Admin

1. Set the `ADMIN_EMAIL` variable in `server/config.env` to the email you want to use for the admin account.

    ```env
    ADMIN_EMAIL=<your email>
    ADMIN_PASSWORD=<your password>
    ```

### Fake User

1. Set the `FAKE_EMAIL` variable in `server/config.env` to the email you want to use for the fake user account.

    ```env
    FAKE_EMAIL=<your email>
    FAKE_PASSWORD=<your password>
    ```

## Database Setup

Setting up and managing the database is crucial for the application's functionality.

1. In your terminal you need to create the database for the selected flask_config environment. 
    
    `python manage.py recreate_db`

2. You need to populate your database with admin and fake user accounts. For flask_configs other than production, you can run the following command to populate your database with admin and fake user accounts (development, testing, unittest). 
    
    `python manage.py setup_dev`

For production, you need to run the following command to populate your database with admin and fake user accounts.

    `python manage.py setup_prod`


3. Initiate Flask migrate so that if you make changes to your code that need to be reflected in to database, those changes can be done in development environment and pushed to production
    
        `python manage.py db init`

4. Create a migration file for the changes you made to the database

        `python manage.py db migrate -m "Initial Migration`



## Manage

This section covers running the server and updating the database schema.

### Run the Server

Execute `python manage.py runserver` to start the server.

### Make updates to database using flask migrate

1. Make changes to your code that need to be reflected in to database

2. Create a migration file for the changes you made to the database

        `python manage.py db migrate -m "<Add comment with changes made>"`

3. Apply the migration to the database

        `python manage.py db upgrade`

4. Go to your production server and run the following command to apply the migration to the production database

        `python manage.py db upgrade`

5. To revert the migration, run the following command

        `python manage.py db downgrade`

### API Documentation

To see API documentation, run the server and navigate to

`http://localhost:5000//apidocs`

or whatever port you are running the server on.

This uses flasgger to generate the documentation.

### To format all of your projects files (imports, whitespace, etc.) run the following command

        `python manage.py format`

### Unit Testing

To run unit tests, execute `python manage.py test` in your terminal.

To run unit tests of a specific file or directory, execute `python manage.py test --file=<file or directory path>` in your terminal.

### Helpful Scripts

There is a directory called 'scripts/' in the root project folder. This directory contains the following helpful general scripts:

**Note:** Instructions on how to run these scripts are in the respective file

| File Name | Description | 
| --------------- | -----| 
| clean_tree_linux.py | This file takes a tree.txt produced by linux tree command and cleans it up to show directory structure|

# Folder Structure Explained

**Models (models/):**<br>
Contains classes and functions that directly interact with your database.
Think of it as a representation of your data structure in code, mirroring tables in your database.

**Services (services/):** <br>
Houses the core business logic of your application.
This is where you write code that processes data, makes decisions, and performs the main operations of your application.

**API (api/):** <br>
Contains the definitions of your API endpoints.
This is where you define how external clients (like your frontend) interact with your application, usually through HTTP requests.

**Handler (handler/):** <br>
Manages incoming HTTP requests and directs them to the appropriate service.
Think of it as a traffic controller, interpreting requests and determining the response flow.

**Schema (schema/):** <br>
Defines the structure of your data for validation purposes.
It ensures that the data coming into your application (from users, external services, etc.) meets a certain format or set of rules.

**Middleware (middleware/):** <br>
Contains functions that execute during the request/response cycle, but outside of your main business logic.
Typically used for tasks like logging, authentication, or modifying request/response objects.

**Types (types/):** <br>
Used for defining custom data types or structures that you want to use across your application.
Helpful in maintaining consistency and clarity in how data is structured and passed around.

**Utils (utils/):** <br>
A collection of helper functions or constants that don’t fit neatly into other categories.
These are usually generic functions used in multiple places in your application.

**Migrations (migrations/):** <br>
If you're using an ORM (Object-Relational Mapping) tool like SQLAlchemy, this directory would contain migration scripts to manage database schema changes.

**Static (static/):** <br>
For serving static files like images, CSS, and JavaScript (if your backend serves any frontend content).

**Templates (templates/):** <br>
If your application renders HTML on the server side, this directory would contain HTML templates.


## Contributing

Interested in contributing? We welcome pull requests and issues from developers of all skill levels.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
