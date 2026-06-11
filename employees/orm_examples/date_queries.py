from employees.models import Employee
from tasks.models import Task


# 51. dates()
Employee.objects.dates(
    "joining_date",
    "year"
)


# 52. datetimes()
Task.objects.datetimes(
    "created_at",
    "month"
)