from django.db import transaction

from employees.models import Employee
from tasks.models import Task


# 19. select_for_update()
with transaction.atomic():

    employee = (
        Employee.objects
        .select_for_update()
        .get(id=1)
    )


# 31. nowait
Employee.objects.select_for_update(
    nowait=True
)


# 32. skip_locked
Task.objects.select_for_update(
    skip_locked=True
)


# 33. of=
Employee.objects.select_related(
    "department"
).select_for_update(
    of=("self",)
)


# 34. none()
Employee.objects.none()