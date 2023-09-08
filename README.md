# SoftDesk


SoftDesk is a web application that helps teams manage projects, issues, and collaborate effectively. It's built with Django and Django REST framework.

## Features

- User authentication and authorization with JWT tokens.
- Project creation and management.
- Create and assign issues within a project.
- Add comments to issues.
- Prioritize and tag issues.
- Project contributors and permissions.
- Full control for project authors.

## Requirements

- Python 3.x
- Django
- Django REST framework
- djangorestframework-simplejwt (for JWT authentication)

## Installation

1. Clone the repository:
````
git clone https://github.com/azer7777/Project-10.git
````
2. Create a virtual environment and activate it:
````
python3 -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3. Install dependencies:
````
pip install -r requirements.txt
````
4. Run migrations:
````
cd SoftDesk
python manage.py migrate
````
5. Create a superuser to manage the admin panel:
````
python manage.py createsuperuser
````
6. Start the development server:
````
python manage.py runserver
````
7. Access the application in your browser at http://localhost:8000.

## Usage

Register and log in to your account.
Create a project and become its author.
Add contributors to the project.
Create issues within the project.
Assign issues to contributors.
Add comments to issues.
Manage your projects and issues effectively!

## API Endpoints
SoftDesk provides a RESTful API for managing projects, issues, and comments. You can explore the API endpoints by visiting http://localhost:8000/api/ after running the development server.
