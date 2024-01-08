# Django Employees API

This is a Django-based RESTful API for managing employees.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python and pip installed on your machine. Additionally, it's recommended to use a virtual environment to manage dependencies.

```bash
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
## Django  Setup
```bash
# Install django
pip install django

# install Restframe-work
pip install djangorestframework

# Database Setup
python manage.py makemigrations
python manage.py migrate

# Running the Development Server
python manage.py runserver

```

##### The API will be accessible at http://localhost:8000/.

### API Endpoints
- `/api/employees/`: List and create employees.

## Built With
- Django - The web framework for perfectionists with deadlines.
- Django REST framework - A powerful and flexible toolkit for building Web APIs.
