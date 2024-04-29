# Backend

The backend of this full-stack web application is built using Python Flask and SQLAlchemy. It provides a RESTful API for the frontend to interact with and handles data management and business logic.

## Overview

This backend is designed to be a scalable and modular foundation for building web applications. It utilizes SQLAlchemy for database management and supports multiple environments, including development, testing, unit testing, and production.

### Key Features

- Database Management: Utilizes SQLAlchemy ORM for efficient and flexible database interactions.
- Environments: Supports development, testing, unit testing, and production environments.
- Middleware: Includes an API logger and a response manipulator for enhanced monitoring and control of API interactions.
- Logging: Implemented using Loguru, providing robust logging capabilities for debugging and monitoring.
- Unit Testing: Extensive coverage for services, ensuring code reliability and performance.
- Handlers: Supports rate limiting to ensure application stability under high load.

### APIs

The backend provides the following APIs:

- User
  - Register: Allows new users to create an account.
  - Delete: Enables users to remove their account.
  - Update: Provides functionality for users to update their account details.

To view the API documentation, run the server and navigate to:
- Swagger JSON: `http://localhost:5000/apispec_1.json`
- Swagger UI: `http://localhost:5000/apidocs`

Replace the port `5000` with the appropriate port number if you're using a different one.

## Getting Started

To set up and run the backend, follow these steps:

1. Navigate to the `backend/` directory:
```cd backend```
2. Create a virtual environment:
```python3 -m venv venv```
3. Activate the virtual environment:
- For Linux/Mac:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```

4. Install Python dependencies:
```pip install -r requirements.txt```
5. Configure the backend:
- Create a `config.env` file in the `server/` directory.
- Set the following variables in the `config.env` file:
  ```
  APP_NAME='Your App Name'
  SECRET_KEY='Your Secret Key'
  FLASK_CONFIG=development
  DATABASE_URL=data-dev.sqlite
  LOGGING_LEVEL='DEBUG'
  ADMIN_EMAIL='admin@example.com'
  ADMIN_PASSWORD='admin_password'
  FAKE_EMAIL='fake@example.com'
  FAKE_PASSWORD='fake_password'
  FRONTEND_ORIGIN=http://localhost:3000
  ```
- Replace the placeholders with your own values.

6. Set up the database:
- Create the database:
  ```
  python manage.py recreate_db
  ```
- Populate the database with admin and fake user accounts:
  - For development, testing environments:
    ```
    python manage.py setup_dev
    ```
  - For production environment:
    ```
    python manage.py setup_prod
    ```
- Initialize Flask migrate:
  ```
  python manage.py db init
  ```
- Create a migration file for database changes:
  ```
  python manage.py db migrate -m "Initial Migration"
  ```

7. Run the server:
```python manage.py runserver```
The backend server should now be running at `http://localhost:5000` (or the appropriate URL).

## Configuration

The backend configuration is managed through the `config.env` file located in the `server/` directory. Here's a description of each configuration variable:

- `APP_NAME`: The name of your application.
- `SECRET_KEY`: A secret key used for securely signing the session cookie and other security-related needs.
- `FLASK_CONFIG`: The environment configuration for Flask. Options include `development`, `testing`, `unit_testing`, and `production`.
- `DATABASE_URL`: The URL or path to the database file (e.g., `data-dev.sqlite` for SQLite).
- `LOGGING_LEVEL`: The logging level for the application. Options include `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- `ADMIN_EMAIL`: The email address for the admin user account.
- `ADMIN_PASSWORD`: The password for the admin user account.
- `FAKE_EMAIL`: The email address for the fake user account (used for testing and development).
- `FAKE_PASSWORD`: The password for the fake user account.
- `FRONTEND_ORIGIN`: The origin URL of the frontend application (e.g., `http://localhost:3000`).

Make sure to update these variables according to your specific configuration requirements.

## Database Management

The backend uses SQLAlchemy for database management. To make updates to the database schema and apply migrations, follow these steps:

1. Make changes to your code that need to be reflected in the database.

2. Create a migration file for the changes:
```python manage.py db migrate -m "Description of the changes"```
3. Apply the migration to the database:
```python manage.py db upgrade```
4. If you need to revert the migration, run:
```python manage.py db downgrade```
## Unit Testing

The backend includes unit tests to ensure the reliability and performance of the code. To run the unit tests, execute the following command:
```python manage.py test```
To run unit tests for a specific file or directory, use:
```python manage.py test --file=<file_or_directory_path>```
## Code Formatting

To format all the project files (imports, whitespace, etc.), run the following command:
```python manage.py format```
This helps maintain a consistent code style throughout the project.

## Folder Structure

The backend folder structure is organized as follows:
```
backend/
├── data/
├── server/
│   ├── apis/
│   ├── handlers/
│   ├── integrations/
│   ├── middlewares/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── types/
│   └── utils/
├── tests/
├── config.env
├── data-dev.sqlite
├── manage.py
└── requirements.txt
```
- The `data/` directory contains the SQLite database files for different environments.
- The `server/` directory contains the main application code.
  - `apis/`: Defines the API endpoints and their respective handlers.
  - `handlers/`: Implements the logic for handling API requests and responses.
  - `integrations/`: Contains code for integrating with external services or systems.
  - `middlewares/`: Defines middleware functions for request/response processing.
  - `models/`: Represents the database models and their relationships.
  - `schemas/`: Defines the schema validators for request/response data.
  - `services/`: Implements the business logic and data manipulation.
  - `static/`: Serves static files, such as images or CSS.
  - `templates/`: Contains HTML templates for server-side rendering (if applicable).
  - `types/`: Defines custom data types or structures used across the application.
  - `utils/`: Contains utility functions and helper modules.
- The `tests/` directory contains unit tests for the backend code.
- The `config.env` file stores the configuration variables for the backend.
- The `data-dev.sqlite` file is the SQLite database used for development.
- The `manage.py` file is the entry point for running the backend server and management commands.
- The `requirements.txt` file lists the Python dependencies required for the backend.

## Contributing

Contributions to the backend are welcome! If you find any issues or have suggestions for improvements, please [open an issue](https://github.com/your-repo/issues) or submit a pull request. Make sure to follow the existing code style and include appropriate tests with your changes.

## License

This backend is open-source and available under the [MIT License](../LICENSE.md). Feel free to use, modify, and distribute it as per the terms of the license.

## Support

If you have any questions or need assistance with the backend, please [open an issue](https://github.com/your-repo/issues) on the GitHub repository. We'll be happy to help!

Happy coding!