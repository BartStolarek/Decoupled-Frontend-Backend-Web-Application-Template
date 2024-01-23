
1. In order for Flask to run, there must be a `SECRET_KEY` variable declared. Generating one is simple with Python 3:

   ```
   $ python3 -c "import secrets; print(secrets.token_hex(16))"
   ```

   This will give you a 32-character string. Copy this string and add it to your `config.env`:

   ```
   SECRET_KEY=Generated_Random_String
   ```

2. The mailing environment variables can be set as the following.
   We recommend using [Sendgrid](https://sendgrid.com) for a mailing SMTP server, but anything else will work as well.

   ```
   MAIL_USERNAME=SendgridUsername
   MAIL_PASSWORD=SendgridPassword
   ```

Other useful variables include:

| Variable        | Default   | Discussion  |
| --------------- |-------------| -----|
| `ADMIN_EMAIL`   | `flask-base-admin@example.com` | email for your first admin account |
| `ADMIN_PASSWORD`| `password`                     | password for your first admin account |
| `REDISCLOUD_URL` | `http://localhost:6379`        | [Redis To Go](https://redistogo.com) URL or any redis server url |
| `RAYGUN_APIKEY` | `None`                         | API key for [Raygun](https://raygun.com/raygun-providers/python), a crash and performance monitoring service |

###### Database Connections

Database instances should be isolated to different environments, and this is set by the variables `DATABASE_URL` (key) and `FLASK_CONFIG` (key). 

<br>
<br>

Variable: `FLASK_CONFIG` 
| Options (Value)        | Discussion  |
| --------------- | -----|
| `default`   | Default environment, has destinations as development |
| `development` |  Development environment run locally with dev database (sqlite) being stored locally |
| `testing`  | Testing environment run locally with test database (sqlite) being stored locally |
| `unix`  | ??TODO??  |
| `production`  | Production environment runs locally but connects to deployed (production) database (postgres) on heroku |
| `heroku`  | Heroku environment designed to run on heroku host and connects to production database (postgres) |

<br>
<br>


Variable: `DATABASE_URL`
| Options (Value)        | Discussion  |
| --------------- | -----|
| `data-dev.sqlite`   | Development dedicated database stored locally using sqlite |
| `data-test.sqlite` |  Testing dedicated database stored locally using sqlite |
| postgres URL  | Production dedicated database stored on Heroku |
| any other Database URL  | Production dedicated database stored on Heroku |


Models (models/):
Contains classes and functions that directly interact with your database.
Think of it as a representation of your data structure in code, mirroring tables in your database.

Services (services/):
Houses the core business logic of your application.
This is where you write code that processes data, makes decisions, and performs the main operations of your application.

API (api/):
Contains the definitions of your API endpoints.
This is where you define how external clients (like your frontend) interact with your application, usually through HTTP requests.

Handler (handler/):
Manages incoming HTTP requests and directs them to the appropriate service.
Think of it as a traffic controller, interpreting requests and determining the response flow.

Schema (schema/):
Defines the structure of your data for validation purposes.
It ensures that the data coming into your application (from users, external services, etc.) meets a certain format or set of rules.

Middleware (middleware/):
Contains functions that execute during the request/response cycle, but outside of your main business logic.
Typically used for tasks like logging, authentication, or modifying request/response objects.

Types (types/):
Used for defining custom data types or structures that you want to use across your application.
Helpful in maintaining consistency and clarity in how data is structured and passed around.

Utils (utils/):
A collection of helper functions or constants that don’t fit neatly into other categories.
These are usually generic functions used in multiple places in your application.

Migrations (migrations/):
If you're using an ORM (Object-Relational Mapping) tool like SQLAlchemy, this directory would contain migration scripts to manage database schema changes.

Static (static/):
For serving static files like images, CSS, and JavaScript (if your backend serves any frontend content).

Templates (templates/):
If your application renders HTML on the server side, this directory would contain HTML templates.

# For migration use:
# - make changes to models
# - make sure env* is removed from gitignore
# - python manage.py db migrate -m "added positive EV table"
# - git add .
# - git commit -m ""
# - git push && git push heroku master
# - heroku run python manage.py db upgrade