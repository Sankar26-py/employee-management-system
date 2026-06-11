import pytest #type: ignore
from datetime import date

from employees.models import Department, Employee


@pytest.mark.django_db
def test_high_salary_manager():

    department = Department.objects.create(
        name="IT",
        budget=1000000
    )

    Employee.objects.create(
        name="John",
        email="john@test.com",
        gender="male",
        salary=150000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    Employee.objects.create(
        name="Jane",
        email="jane@test.com",
        gender="female",
        salary=40000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    assert Employee.objects.high_salary().count() == 1