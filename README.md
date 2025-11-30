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

## Technologies & Tools

- **Python 3.11.4** – programming language for backend logic
- **Django 5.2.8** – web framework
- **Django REST Framework 3.16.1** – REST API development
- **PostgreSQL** – relational database
  - `psycopg3`, `psycopg-binary`, `psycopg2-binary` – PostgreSQL adapters
- **Redis 7.1.0** – caching and Celery broker
- **django-redis 6.0.0** – Django cache integration with Redis
- **Celery** – asynchronous task queue (if used)
- **Pillow 12.0.0** – image handling
- **drf-yasg 1.21.11** – API documentation (Swagger/OpenAPI)
- **djangorestframework-simplejwt 5.5.1** – JWT authentication
- **django-environ 0.12.0** & **python-decouple 3.8** – environment configuration
- **inflection 0.5.1** – string conversion utilities (camelize, underscore, pluralize)
- **asgiref 3.10.0** – ASGI support for Django
- **certifi 2025.11.12** – SSL certificates
- **charset-normalizer 3.4.4** – encoding handling
- **idna 3.11** – international domain names / URL encoding
- **packaging 25.0** – version parsing
- **pytz 2025.2** & **tzdata 2025.2** – timezone support
- **PyJWT 2.10.1** – JWT handling
- **pywin32 311** – Windows extensions
- **PyYAML 6.0.3** – YAML parsing
- **requests 2.32.5** – HTTP requests
- **sqlparse 0.5.3** – SQL formatting
- **uritemplate 4.2.0** – URI template handling
- **docker 7.1.0** – Python client for Docker integration


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
        'NAME': 'alx_project_nexus_db',
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

### ERD Diagram  
[**View Here**](https://drive.google.com/file/d/11xI2eXLY5Hc-NfuPPWPswK7u7wbjTXwe/view?usp=sharing)

API Endpoints

#Authentication & User Accounts
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/token/	Obtain JWT access & refresh tokens
POST	/api/token/refresh/	Refresh access token

#Category API Endpoints
#Public Endpoints
Method	Endpoint	Description
GET	/api/categories/	List all categories
GET	/api/categories/<int:pk>/	Retrieve a single category

#Admin Endpoints
Method	Endpoint	Description
POST	/api/categories/create/	Create a new category
PUT	/api/categories/<int:pk>/update/	Update category details
DELETE	/api/categories/<int:pk>/delete/	Delete a category

#Product API Endpoints
#Public Endpoints
Method	Endpoint	Description
GET	/api/products/	List all products (cached, searchable, paginated)
GET	/api/products/<int:pk>/	Retrieve a single product

#Admin Endpoints
Method	Endpoint	Description
POST	/api/products/create/	Create a new product
PUT	/api/products/<int:pk>/update/	Update product details
DELETE	/api/products/<int:pk>/delete/	Delete a product

Contributing
Contributions are welcome!

Fork the repository

Create a branch (git checkout -b feature-name)

Make changes and commit (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.