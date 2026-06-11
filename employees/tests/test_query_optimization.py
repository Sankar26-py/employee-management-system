import pytest #type: ignore

from django.db import connection
from django.test.utils import CaptureQueriesContext

from employees.models import Employee
from employees.tests.factories import EmployeeFactory


@pytest.mark.django_db
def test_select_related_uses_single_query():

    EmployeeFactory.create_batch(5)

    with CaptureQueriesContext(connection) as ctx:

        list(
            Employee.objects.select_related(
                "department"
            )
        )

    assert len(ctx) == 1