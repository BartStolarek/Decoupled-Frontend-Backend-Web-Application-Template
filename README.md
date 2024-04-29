# Full-Stack Web Application Template

This repository serves as a template for a decoupled full-stack web application. The frontend is built with React Next.js and Tailwind CSS, while the backend is developed using Python Flask and SQLAlchemy.

## Overview

This project provides a starting point for building a modern, decoupled web application. The frontend and backend are developed independently, allowing for flexibility and scalability. The template is designed to expedite the setup process and provide a solid foundation for further development.

### Frontend

The frontend is located in the `frontend/` directory and is built using the following technologies:

- React Next.js: A powerful framework for building server-rendered React applications
- Tailwind CSS: A utility-first CSS framework for rapidly building custom designs
- DaisyUI: A plugin for Tailwind CSS that provides a set of pre-designed UI components

Key features of the frontend include:

- Server-side rendering for improved performance and SEO
- Modular and reusable React components
- Responsive and customizable UI with Tailwind CSS
- Pre-designed UI components using DaisyUI
- Easy integration with the backend API

For more information about the frontend, please refer to the `frontend/README.md` file.

### Backend

The backend is located in the `backend/` directory and is built using the following technologies:

- Python Flask: A lightweight and flexible web framework for building APIs
- SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) library
- Swagger: An open-source software framework for designing, building, and documenting RESTful APIs

Key features of the backend include:

- RESTful API architecture
- Multiple environments support (development, testing, unit testing, and production)
- Database management using SQLAlchemy ORM
- API logging and response manipulation middleware
- Robust logging with Loguru
- Extensive unit testing coverage for services
- Rate limiting for API endpoints

For more information about the backend, please refer to the `backend/README.md` file.

## Getting Started

To get started with this template, follow these steps:

1. Clone the repository:
```git clone [repository URL]```
2. Navigate to the project directory:
```cd [project directory]```
3. Set up the backend:
- Navigate to the `backend/` directory:
  ```
  cd backend
  ```
- Create a virtual environment:
  ```
  python3 -m venv venv
  ```
- Activate the virtual environment:
  - For Linux/Mac:
    ```
    source venv/bin/activate
    ```
  - For Windows:
    ```
    venv\Scripts\activate
    ```
- Install Python dependencies:
  ```
  pip install -r requirements.txt
  ```
- Configure the backend by following the instructions in the `backend/README.md` file.

4. Set up the frontend:
- Navigate to the `frontend/` directory:
  ```
  cd frontend
  ```
- Install dependencies:
  ```
  npm install
  ```
- Configure the frontend by following the instructions in the `frontend/README.md` file.

5. Start the development servers:
- For the backend:
  - Navigate to the `backend/` directory:
    ```
    cd backend
    ```
  - Run the server:
    ```
    python manage.py runserver
    ```
- For the frontend:
  - Navigate to the `frontend/` directory:
    ```
    cd frontend
    ```
  - Build the CSS:
    ```
    npm run build:css
    ```
  - Start the development server:
    ```
    npm run dev
    ```

6. Access the application:
- Frontend: Open your browser and visit `http://localhost:3000` (or the appropriate URL)
- Backend API: The API endpoints can be accessed at `http://localhost:5000` (or the appropriate URL)

## Project Structure

The project structure is organized as follows:
```
├── backend/
│   ├── data/
│   ├── server/
│   │   ├── apis/
│   │   ├── handlers/
│   │   ├── integrations/
│   │   ├── middlewares/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── types/
│   │   └── utils/
│   ├── tests/
│   ├── config.env
│   ├── data-dev.sqlite
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles/
│   │   └── utils/
│   ├── .env
│   ├── .gitignore
│   ├── next.config.js
│   ├── package.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   └── tsconfig.json
├── .gitignore
├── LICENSE.md
└── README.md
```

- The `backend/` directory contains the Python Flask backend code and related files.
- The `frontend/` directory contains the React Next.js frontend code and related files.
- The `.gitignore` file specifies the files and directories that should be ignored by Git.
- The `LICENSE.md` file contains the license information for the project.
- The `README.md` file provides an overview and instructions for the project.

## Contributing

Interested in contributing? We welcome pull requests and issues from developers of all skill levels. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive commit messages
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

Please ensure that your code follows the project's coding conventions and includes appropriate tests.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for more information.

## Acknowledgements

We would like to thank the following projects and resources that have inspired and contributed to the development of this template:

- [React Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI](https://daisyui.com/)
- [Python Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Swagger](https://swagger.io/)

## Support

If you encounter any issues or have questions regarding this template, please [open an issue](https://github.com/your-repo/issues) on the GitHub repository. We'll do our best to assist you.

Happy coding!