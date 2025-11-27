# ALX PROJECT NEXUS

An e-commerce web application built with Django and PostgreSQL.  
Allows users to browse products, manage carts, place orders, and handle payments securely.


## Project Overview

ALX Project Nexus is a Django-based e-commerce platform featuring:

- User authentication and profiles
- Product catalog with categories
- Shopping cart and checkout
- Order management and tracking
- PostgreSQL database integration
- API endpoints for front-end or mobile integration

---

## Features

- User registration and login
- Profile management with optional profile picture
- CRUD operations for products and categories
- Shopping cart system
- Order placement and tracking
- Payment simulation
- Admin panel for managing products, categories, and users

---

## Technologies

- Python 3.11.4
- Django 5.2.8
- Django REST Framework 3.16.1
- PostgreSQL (psycopg3 / psycopg2-binary)
- Pillow 12.0.0 (image handling)
- drf-yasg 1.21.11 (API documentation)
- django-environ 0.12.0 & python-decouple 3.8 (environment configuration)
- inflection 0.5.1

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Nkamenyin/alx-project-nexus.git
cd alx-project-nexus
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure PostgreSQL database in settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alx_project_nexus',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Usage
Open your browser at http://127.0.0.1:8000

Register a new user or log in

Browse products, add items to cart, and place orders

Access the admin panel at /admin for management

Database Schema
The project uses PostgreSQL with the following main tables:

User / CustomerProfile

Category / Product / ProductImage

Cart / CartItem

Order / OrderItem / Payment

Address

ERD Diagram: View Here

API Endpoints

Endpoint	Method	Description
/api/login/	POST	Log in user
/api/register/	POST	Register new user
/api/products/	GET	List all products
/api/products/<id>/	GET	Product details
/api/cart/	POST	Add item to cart
/api/orders/	GET	List user orders

Contributing
Contributions are welcome!

Fork the repository

Create a branch (git checkout -b feature-name)

Make changes and commit (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.