import pytest #type:ignore
from datetime import date
from django.db.models import Avg

from employees.models import Department, Employee


@pytest.mark.django_db
def test_aggregate_avg_salary():

    department = Department.objects.create(
        name="Finance",
        budget=1000000
    )

    Employee.objects.create(
        name="A",
        email="a@test.com",
        gender="male",
        salary=50000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    Employee.objects.create(
        name="B",
        email="b@test.com",
        gender="male",
        salary=100000,
        joining_date=date(2024, 1, 1),
        department=department
    )

    result = Employee.objects.aggregate(
        avg_salary=Avg("salary")
    )

    assert result["avg_salary"] == 75000