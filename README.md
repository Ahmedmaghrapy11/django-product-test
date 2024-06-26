Follow these steps to install the project locally:

1. Create database on mysql
# CREATE DATABASE django_test;

2. Set Up Database
Configure the database settings in the settings.py file. this project is configured to use MySQL.

3. Clone the Repository
Clone this repository to your local machine using the following command:

# git clone https://github.com/Ahmedmaghrapy11/django-product-test

4. Set Up a Virtual Environment
Navigate to the project directory and set up a virtual environment. You can use virtualenv or venv:

# cd django-project
# python3 -m venv env

Activate the virtual environment:

On macOS/Linux:
# source env/bin/activate

On Windows:
# .\env\Scripts\activate

5. Install Dependencies
Install the project dependencies using pip:

# pip install -r requirements.txt



Run the following commands to apply migrations and create database tables:

# python manage.py makemigrations
# python manage.py migrate

6. Run the Development Server
Start the Django development server:
# python manage.py runserver

The server should now be running locally. You can access the project in your web browser at http://127.0.0.1:8000/.

7. Access the Admin Interface (Optional)
To access the Django admin interface, create a superuser account by running the following command:

python manage.py createsuperuser
Follow the prompts to create a superuser account. You can then access the admin interface at http://127.0.0.1:8000/admin/.
