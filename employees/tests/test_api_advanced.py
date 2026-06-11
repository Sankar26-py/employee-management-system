import pytest #type: ignore

from rest_framework.test import APIClient

from employees.tests.factories import (
    EmployeeFactory
)


@pytest.mark.django_db
def test_employee_list_api():

    EmployeeFactory.create_batch(5)

    client = APIClient()

    response = client.get(
        "/api/employees/"
    )

    assert response.status_code == 200