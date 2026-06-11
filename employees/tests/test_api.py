import pytest #type:ignore
from datetime import date

from rest_framework.test import APIClient

from employees.models import Department, Employee


@pytest.mark.django_db
def test_employee_list_api():

    department = Department.objects.create(
        name="IT",
        budget=1000000
    )

    Employee.objects.create(
        name="John",
        email="john@test.com",
        gender="male",
        salary=50000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    client = APIClient()

    response = client.get("/api/employees/")

    assert response.status_code == 200