from django.db import transaction

from employees.models import Employee
from tasks.models import Task


def run():

    print("\n========== LOCKING & SPECIAL QUERYSETS ==========")

    # 19. select_for_update() Locks rows for update in transactions.
    # Locks selected rows until transaction ends.
    print("\n19. select_for_update()")

    with transaction.atomic():

        employee = (
            Employee.objects
            .select_for_update()
            .get(id=1)
        )

        print(
            f"Locked Employee: "
            f"{employee.name}"
        )

    # 31. nowait=True    # — nowait=True raises immediately if the lock can’t be acquired.
    # Raises an error immediately if row is locked.
    print("\n31. nowait=True")

    try:

        with transaction.atomic():

            employee = (
                Employee.objects
                .select_for_update(nowait=True)
                .first()
            )

            if employee:
                print(
                    f"Locked Employee: "
                    f"{employee.name}"
                )

    except Exception as e:

        print(
            f"Could not acquire lock: "
            f"{e}"
        )

    # 32. skip_locked=True     # – skip_locked=True skips rows already locked by others.
    # Skips rows already locked by another transaction.
    print("\n32. skip_locked=True")

    with transaction.atomic():

        tasks = (
            Task.objects
            .select_for_update(
                skip_locked=True
            )[:5]
        )

        for task in tasks:

            print(
                f"Task: {task.title}"
            )

    # 33. of=('self',)  In PostgreSQL, restricts row‐locking to only the specified tables in a multi‐join query.
    # Lock only Employee table rows,
    # not joined Department rows.
    print("\n33. of=('self',)")

    with transaction.atomic():

        employees = (
            Employee.objects
            .select_related("department")
            .select_for_update(
                of=("self",)
            )[:5]
        )

        for employee in employees:

            print(
                f"{employee.name} -> "
                f"{employee.department.name}"
            )

    # 34. none() Returns an empty queryset of the given model.
    # Returns an empty QuerySet.
    print("\n34. none()")

    employees = Employee.objects.none()

    print(
        f"Employee Count: "
        f"{employees.count()}"
    )