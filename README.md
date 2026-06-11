# Employee Management System

A production-style Django REST Framework project built with PostgreSQL that demonstrates advanced Django ORM concepts, query optimization techniques, REST API development, automated testing, and runnable ORM demonstrations.

---

## Overview

This project was built to showcase real-world Django development skills expected from a Python Django developer with 3+ years of experience.

The project includes:

* Employee Management System
* PostgreSQL Integration
* Django REST Framework APIs
* Advanced ORM Examples
* Query Optimization Techniques
* Custom Managers & QuerySets
* Automated Testing with Pytest
* FactoryBoy Test Data Generation
* Coverage Reporting
* Runnable ORM Demonstrations

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

## Core Modules

### Employees

* Employee CRUD Operations
* Employee Statistics
* Salary Analytics
* Department Assignment

### Departments

* Department Management
* Employee Count Tracking
* Budget Management

### Projects

* Project Tracking
* Employee Assignment
* Project Analytics

### Tasks

* Task Assignment
* Pending Task Tracking
* Completion Monitoring

---

## Advanced Django ORM

This project contains 57+ ORM examples organized by topic.

### Basic Queries

* all()
* filter()
* exclude()
* get()
* order_by()
* values()
* values_list()
* distinct()
* exists()

### Aggregation & Annotation

* aggregate()
* annotate()
* Count()
* Avg()
* Max()
* Min()
* Sum()

### Advanced Queries

* Q Objects
* F Expressions
* Case / When
* Subquery
* OuterRef
* Exists

### Query Optimization

* select_related()
* prefetch_related()
* only()
* defer()

### Bulk Operations

* bulk_create()
* bulk_update()
* update()
* delete()

### PostgreSQL Features

* select_for_update()
* explain()
* Window Functions
* Ranking Queries

### Date Queries

* year lookup
* month lookup
* range lookup
* date filtering

---

## Runnable ORM Demonstrations

All ORM examples can be executed directly from the terminal.

Run:

```bash
python manage.py run_orm_demo
```

This command executes all ORM demonstration modules and displays results using sample PostgreSQL data.

Example Output:

```text
========== BASIC ORM QUERIES ==========

1. all()
2. filter()
3. exclude()

========== ADVANCED ORM QUERIES ==========

Q Objects
Subquery
Exists

========== WINDOW FUNCTIONS ==========

Salary Rank
Department Rank
```

---

## Testing

The project includes automated tests for:

* Models
* Custom Managers
* APIs
* ORM Queries
* Query Optimization

Run all tests:

```bash
python -m pytest -v
```

Example:

```text
6 passed
```

---

## Coverage Report

Generate coverage report:

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

---

## FactoryBoy Support

FactoryBoy is used to generate realistic test data.

Example:

```python
employee = EmployeeFactory()

department = DepartmentFactory()
```

Benefits:

* Cleaner Tests
* Reusable Test Data
* Faster Test Development

---

## Environment Variables

Create a `.env` file:

```env
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Installation

Clone Repository:

```bash
git clone https://github.com/Sankar26-py/employee-management-system.git

cd employee-management-system
```

Create Virtual Environment:

```bash
python -m venv env

env\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

Apply Migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

Create Superuser:

```bash
python manage.py createsuperuser
```

Load Sample Data:

```bash
python scripts/seed_data.py
```

Run Server:

```bash
python manage.py runserver
```

---

## API Endpoints

### Employees

```http
GET     /api/employees/
POST    /api/employees/

GET     /api/employees/high_salary/
GET     /api/employees/salary_stats/
GET     /api/employees/top_performers/
```

### Departments

```http
GET     /api/departments/
POST    /api/departments/
```

### Projects

```http
GET     /api/projects/
GET     /api/projects/active_projects/
GET     /api/projects/project_summary/
```

### Tasks

```http
GET     /api/tasks/
GET     /api/tasks/pending_tasks/
GET     /api/tasks/incomplete_tasks/
```

---

## Project Structure

```text
employee-management-system/

├── employees/
│   ├── models.py
│   ├── managers.py
│   ├── serializers.py
│   ├── views.py
│   ├── orm_examples/
│   ├── management/
│   │   └── commands/
│   │       └── run_orm_demo.py
│   └── tests/
│
├── projects/
├── tasks/
├── scripts/
│   └── seed_data.py
│
├── requirements.txt
├── pytest.ini
├── README.md
├── .gitignore
└── manage.py
```

---

## Future Improvements

* JWT Authentication
* Redis Caching
* Celery Integration
* Docker Support
* GitHub Actions CI/CD
* Swagger Documentation

---

## Author

**Sankar K**

Python Django Developer

GitHub:
https://github.com/Sankar26-py
