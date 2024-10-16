# Products App

## Introduction
This is a Django-based product management application where users can perform CRUD (Create, Read, Update, Delete) operations on products. The app is configured to use MySQL as the database. It features an admin interface for managing products and other related data.

## Technologies
- **Django**: 5.0.6
- **MySQL**: 8.x.x (or any version you are using)
- **Python**: 3.1.0

## Features
- Manage products (create, read, update, delete).
- Admin interface for product management.
- RESTful APIs using Django Rest Framework.
- MySQL database integration.

## Setup

### 1. Create Database in MySQL
Create a new MySQL database for the project:
```sql
CREATE DATABASE django_test;
```

Set Up Database:
```code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### 2. Clone the Repository
```bash
  git clone https://github.com/Ahmedmaghrapy11/django-product-test
  cd django-product-test
```

### 3. Set Up a Virtual Environment
   - On macOS/Linux:
```
    python3 -m venv env
    source env/bin/activate
```
   - On Windows:
```
    python -m venv env
    .\env\Scripts\activate
```
### 4. Install Dependencies
```bash
  pip install -r requirements.txt
```
### 5. Apply Migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

### 6. Run the Development Server
```bash
  python manage.py runserver
```
