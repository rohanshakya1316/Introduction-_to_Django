# Introduction_to_Django
The basic concepts of Python Django framework.


# Django Starter Guide 🐍

This repository will help you get started with Django — a high-level Python web framework that encourages rapid development and clean, pragmatic design.

---

## 📦 Installation

### 1. Clone the Repository (Optional)

git clone https://github.com/your-username/your-repo.git
cd your-repo

### 2. Create a Virtual Environment

pip install virtualenv

virtualenv env

python -m venv env  [For windows]

python3 -m venv env [For Linux and MacOS]

### 3. Activate the Environment

env\Scripts\activate [For Windows]

source env/bin/activate [For macOS/Linux]

### 4. Install Django

pip install django

(Optional) Create a requirements.txt:

pip freeze > requirements.txt

pip install -r requirements.txt [For installing all the package in specified file]

## 🚀 Create a Django Project

django-admin startproject projectname
cd projectname

Your folder structure will look like:

projectname/

    manage.py

    projectname/

        __init__.py

        settings.py

        urls.py

        asgi.py

        wsgi.py

## 🧱 Create a Django App

Inside your project folder:

python manage.py startapp appname

Add the app to INSTALLED_APPS in projectname/settings.py:

INSTALLED_APPS = [
    ...
    'appname',
]

## 🔧 Run Migrations

### Create migration files
python manage.py makemigrations

### Apply them to the database
python manage.py migrate

## 👨‍💻 Run Development Server

python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.

## 📝 Templates Setup
Create a templates folder inside your app:

appname/
    templates/
        appname/
            home.html
In settings.py, update:

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],  # Optional for global templates
        ...
    },
]

Use it in your view:

from django.shortcuts import render

def home(request):
    return render(request, 'appname/home.html')

## 🎨 Static Files (CSS, JS, Images)
Create a folder:

appname/
    static/
        appname/
            style.css
Add this to settings.py:

STATIC_URL = '/static/'

Load static files in templates:

{% load static %}
<link rel="stylesheet" href="{% static 'appname/style.css' %}">

## 🔐 Admin Panel
Create a superuser:

python manage.py createsuperuser

Run the server and visit:

http://127.0.0.1:8000/admin

Register models in admin.py to manage them via the admin interface.

## 📁 Useful Commands
Command	                            Description
python manage.py makemigrations	    Prepares migrations for model changes
python manage.py migrate	        Applies migrations to the DB
python manage.py createsuperuser	Creates an admin user
python manage.py runserver	        Starts development server
python manage.py startapp appname	Creates a new app

## 🧪 Testing Your Setup
Create a simple model in models.py

Run makemigrations and migrate

Add data from Django admin panel

Display data via a view and template

## ✅ Now Ready to Build!
The basics of Django set up is done. From here:

Add models, views, and templates

Set up user authentication

Use forms and validation

Connect with external APIs

## 🛠 Requirements
Python 3.8+

Django 4.x or 5.x

pip