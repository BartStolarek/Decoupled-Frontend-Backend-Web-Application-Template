
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
or
`http://localhost:5000//apidocs`

replace the port 5000 with whatever port you're using.

# How To Use:

This section guides you through setting up and managing your server. Follow the instructions below to get started.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x

## Clone and Initial Setup

To clone and run this project for the first time, follow these steps:
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd [project directory]`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (if you're using linux)
5. Install Python dependencies: `pip install -r requirements.txt`


## Configure

To set up the server, create a `config.env` file in the `server/` directory (not project root directory) with the following variables:

Example config file:
```env
APP_NAME='Flask-React-Boilerplate'
SECRET_KEY=''
FLASK_CONFIG=development
DATABASE_URL=data-dev.sqlite
LOGGING_LEVEL='DEBUG'
ADMIN_EMAIL='noemail@domain.com'
ADMIN_PASSWORD='nopassword'
FAKE_EMAIL='user@fake.com'
FAKE_PASSWORD='fakepassword'
FRONTEND_ORIGIN=http://localhost:5000
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
| postgres URL  | Production dedicated database |

### Logging Level

1. Set the `LOGGING_LEVEL` variable in `server/config.env` to the logging level you want to run the server in.

    ```env
    LOGGING_LEVEL='DEBUG'
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
### CORS Origin

1. Set the `FRONTEND_ORIGIN` variable in `server/config.env` to the origin of your frontend, so that CORS is properly configured to allow requests from your frontend application, ensuring smooth communication between your server and client-side application.

    ```env
    FRONTEND_ORIGIN=http://localhost:5000
    ```

## Database Setup

Setting up and managing the database is crucial for the application's functionality.

1. In your terminal you need to create the database for the selected flask_config environment. 
    
    `python manage.py recreate_db`

2. You need to populate your database with admin and fake user accounts. For flask_configs other than production, you can run the following command to populate your database with admin and fake user accounts (development, testing). 
    
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

### Expose the localhost server to the internet

Using ngrok you can expose your localhost server to the internet. This is useful for testing your server on different devices or connecting to a webflow website. 

1. Download ngrok from the following link: https://ngrok.com/download or for linux execute:

`curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok`

2. Sign up and get your token

3. Authenticate your ngrok agent. You only have to do this once. The Authtoken is saved in the default configuration file. Run this code in your terminal

`ngrok config add-authtoken <token>`

4. Run the following command in your terminal to expose your localhost server to the internet

`ngrok http <your port>`

5. Obtain your ngrok url and use it to connect to your server from any device. It is found under the "Forwarding" section of the ngrok terminal.

6. Remove the visit page warning in your request header by adding the following code in to your request header

`'ngrok-skip-browser-warning': 'true'`

Note: If you find that your ngrok has a authentication failed error because of a limit of 1 agent sessions. You can run:

`pgrep ngrok`

Take the process id and run:

`kill -9 <process id>`

Note: To see ngrok logs you can access:

`http://127.0.0.1:4040`

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

**API (apis/):** <br>
Contains the definitions of your API endpoints.
This is where you define how external clients (like your frontend) interact with your application, usually through HTTP requests.

**Handler (handlers/):** <br>
Manages incoming HTTP requests and directs them to the appropriate service.
Think of it as a traffic controller, interpreting requests and determining the response flow.

**Integration (integrations/):** <br>
Contains code that interacts with external services or systems.

**Schema (schemas/):** <br>
Defines the structure of your data for validation purposes.
It ensures that the data coming into your application (from users, external services, etc.) meets a certain format or set of rules.

**Middleware (middlewares/):** <br>
Contains functions that execute during the request/response cycle, but outside of your main business logic.
Typically used for tasks like logging, authentication, or modifying request/response objects.

**Types (types/):** <br>
Used for defining custom data types or structures that you want to use across your application.
Helpful in maintaining consistency and clarity in how data is structured and passed around.

**Utils (utils/):** <br>
A collection of helper functions or constants that don’t fit neatly into other categories.
These are usually generic functions used in multiple places in your application.

**Static (static/):** <br>
For serving static files like images, CSS, and JavaScript (if your backend serves any frontend content).

**Templates (templates/):** <br>
If your application renders HTML on the server side, this directory would contain HTML templates.


## Contributing

Interested in contributing? I welcome pull requests and issues from developers of all skill levels.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


# Road Map

Currently I'm working on a branch called 'frontend' which adds in a de coupled front end server using Flask.
This will include the general foundations to a webpage that has a user management system.
It will utilise Tailwind css and potentially daisyUI for components.

The goal is to have a independent frontend and backend in the same git, which you could just delete the frontend folder or the server folder, and the remaining
will still run smoothly. 

## Tailwind

### Installation

1. Check that node and npm are installed by using these commands in your terminal `node -v` and `npm -v`, to get a version number.
2. Navigate to the 'frontend' directory `cd frontend`
3. run `npm init -y` to create a package.json file
4. Install tailwind css via npm with `npm install @tailwindcss/latest @tailwindcss/forms @tailwindcss/typography -D postcss-import`
5. Generate tailwind configuration file with `npx tailwindcss init`, this creates a tailwind.config.js file.
6. Run following code to create necessary css files 
```
echo '"tailwindcss/base";\n@import "tailwindcss/components"; \n@import "tailwindcss/utilities";' > static/css/style.css
```
7. Go to frontend/package.json file and add a build script under "scripts", that looks like this:
```
"scripts": {
  "build:css": "tailwindcss -i ./static/css/style.css -o ./static/css/output.css --minify",
  "watch:css": "tailwindcss -i ./static/css/style.css -o ./static/css/output.css --watch"
}

```
8. Go to tailwind.config.js and in the plugins section add `require("@tailwindcss/typography"),`

### Management

1. Change to frontend directory with `cd frontend` from root directory
2. run `npm run build:css` to build the css file
3. run `npm run watch:css` to watch the css file for changes and not need to do it everytime you make changes
3. Include `<link rel="stylesheet" href="{{ url_for('static', filename='css/output.css') }}">` in flask html template files

## daisyUI

### Installation

1. Make sure you're in the frontend directory with your terminal (`cd frontend`)
2. Install daisyUI using terminal `npm i -D daisyui@latest`
3. Add daisyUI to your tailwind.config.js file
```
module.exports = {
  //...
  plugins: [require("daisyui")],
}
```
4. Run `npm run build:css` to build the css file

### Management

Add as an example `<button class="btn btn-primary">Click me</button>` to a template html file like home.html

#### Access Style Guide
To check your websites style guide you can access `http://localhost:3000/styleguide` or whatever port you are running the server on.

#### Update theme colours
1. Access tailwindcss.config.js file
2. go to the const 'myColors' and update the colours to your liking
```const myColors = {
  text: 'rgb(8, 28, 24)', // Usually best to have a monochrome (black to white)
  background: 'rgb(243, 255, 252)',
  primary: 'rgb(72, 203, 171)',
  secondary: 'rgb(152, 159, 226)',
  accent: 'rgb(130, 96, 210)',
  neutral: "rgb(8, 28, 24, 0.15)", // 15% opacity of text is usually good for neutral
  info: "#48a4cb",
  success: "#96D05D",
  warning: "#EDB95E", 
  error: "#E2363F",
};
```

This way, when you are using the daisyUI components and tailwind components, to colour something you just need to add the class `bg-primary` or `text-primary` etc to the class of the element in the html. For example:
    
    `<button class="btn btn-primary">Click me</button>`
    `<div class="bg-accent"></div>`



# React

## Installation

1. Check that node and npm are installed by using these commands in your terminal `node -v` and `npm -v`, to get a version number.
2. 

