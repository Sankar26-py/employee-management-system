import pytest#type: ignore
from datetime import date

from employees.models import Department, Employee


@pytest.mark.django_db
def test_create_department():

    department = Department.objects.create(
        name="IT",
        budget=1000000
    )

    assert department.name == "IT"


@pytest.mark.django_db
def test_create_employee():

    department = Department.objects.create(
        name="HR",
        budget=500000
    )

    employee = Employee.objects.create(
        name="John",
        email="john@test.com",
        gender="male",
        salary=60000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    assert employee.name == "John"
    assert employee.department.name == "HR"