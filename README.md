# Employee Management System

A production-style Django REST Framework project demonstrating advanced PostgreSQL ORM queries, custom managers, API development, query optimization, and automated testing.

---

## Tech Stack

* Python 3.14
* Django 6.0.6
* Django REST Framework 3.17.1
* PostgreSQL
* Faker
* Factory Boy
* Pytest
* Pytest-Django
* Pytest-Cov
* Python-Dotenv

---

## Features

### Employee Management

* Departments
* Employees
* Projects
* Tasks
* Employee Project Assignment

### Advanced Django ORM

This project contains 57+ ORM examples covering:

* filter()
* exclude()
* get()
* values()
* values_list()
* annotate()
* aggregate()
* select_related()
* prefetch_related()
* Q Objects
* F Expressions
* Case / When
* Subquery
* Exists
* OuterRef
* Window Functions
* Rank()
* RowNumber()
* bulk_create()
* bulk_update()
* select_for_update()
* explain()

### PostgreSQL Features

* Row Locking
* Query Planning
* Window Functions
* Aggregations
* Query Optimization

### Testing

* Model Tests
* Manager Tests
* API Tests
* Query Optimization Tests
* FactoryBoy Fixtures
* Coverage Reports

---

## Project Structure

```text
employee-management-system/

├── employees/
│   ├── models.py
│   ├── managers.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── orm_examples/
│   └── tests/
│
├── projects/
│
├── tasks/
│
├── scripts/
│   └── seed_data.py
│
├── requirements.txt
├── pytest.ini
├── README.md
├── .gitignore
├── .env
│
└── manage.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Sankar26-py/employee-management-system.git

cd employee-management-system
```

### Create Virtual Environment

Windows

```bash
python -m venv env

env\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv env

source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

The application loads these variables automatically using `python-dotenv`.

---

## Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE employee_db;
```

Apply migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

---

## Seed Sample Data

Populate the database with sample departments, employees, projects, and tasks.

```bash
python scripts/seed_data.py
```

Generated Data:

* 6 Departments
* 200 Employees
* 50 Projects
* 1000 Tasks
* Employee Project Mappings

---

## Run Development Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## API Endpoints

### Departments

```http
GET    /api/departments/
POST   /api/departments/
```

### Employees

```http
GET    /api/employees/
POST   /api/employees/

GET    /api/employees/high_salary/
GET    /api/employees/top_performers/
GET    /api/employees/salary_stats/
```

### Projects

```http
GET    /api/projects/

GET    /api/projects/active_projects/

GET    /api/projects/project_summary/
```

### Tasks

```http
GET    /api/tasks/

GET    /api/tasks/pending_tasks/

GET    /api/tasks/incomplete_tasks/
```

---

## Running Tests

Run all tests:

```bash
python -m pytest -v
```

Example:

```text
6 passed in 2.10s
```

---

## Coverage Report

Run coverage:

```bash
python -m pytest --cov=employees
```

Generate HTML report:

```bash
python -m pytest --cov=employees --cov-report=html
```

Open:

```text
htmlcov/index.html
```

in your browser.

---

## ORM Examples

Location:

```text
employees/orm_examples/
```

Includes examples for:

* Basic Queries
* Advanced Queries
* PostgreSQL Queries
* QuerySet Helpers
* Bulk Operations
* Window Functions
* Interview Questions

---

## Future Improvements

* JWT Authentication
* Redis Caching
* Celery Background Tasks
* Docker Support
* GitHub Actions CI/CD
* Swagger / OpenAPI Documentation

---

## Author

**Sankar K**

Python Django Developer

GitHub:
https://github.com/Sankar26-py
