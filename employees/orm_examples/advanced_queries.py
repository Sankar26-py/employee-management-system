from django.db.models import (
    Q,
    F,
    Case,
    When,
    Value,
    Exists,
    OuterRef,
    Subquery,
)

from employees.models import Employee
from tasks.models import Task


def run():

    print("\n========== ADVANCED ORM QUERIES ==========")

    # 22. Q()
    # What
    # — Builds complex lookups (especially OR‐ and NOT‐combinations) that can’t be expressed with simple keyword filters.

    # When
    # — You need to combine filters with OR, AND, or negate them.
    # Allows complex OR, AND, NOT conditions.
    print("\n22. Q()")

    employees = Employee.objects.filter(Q(salary__gt=100000) |Q(gender="female"))

    for employee in employees[:5]:
        print(employee.name,employee.salary,employee.gender)

    # 23. F()
    #What
    #— References model fields directly in queries, allowing field‐to‐field comparisons or database‐side arithmetic.

    #When
    #— You want to compare one field to another, or update a field relative to its current value.
    print("\n23. F()")

    tasks = Task.objects.filter(completed_hours__lt=F("estimated_hours"))

    for task in tasks[:5]:
        print(
            task.title,
            f"{task.completed_hours}/{task.estimated_hours}"
        )

    # 24. Case / When
    #What
    #— Constructs conditional expressions (SQL CASE) to annotate or update rows differently based on criteria.

    #When
    #— You need to bucket or transform values in a single query.
    # Adds a calculated field using SQL CASE.
    print("\n24. Case / When")

    employees = Employee.objects.annotate(
        salary_grade=Case(
            When(
                salary__gte=150000,
                then=Value("A")
            ),
            When(
                salary__gte=100000,
                then=Value("B")
            ),
            default=Value("C")
        )
    )

    for employee in employees[:5]:
        print(
            employee.name,
            employee.salary,
            employee.salary_grade
        )

    # 25. Subquery()
    #What
    #— Embeds one queryset inside another (a sub‐SELECT) and refers to the outer query’s fields.

    # When
    #— You need row‐by‐row data from a related table in an annotation or filter.
    # Fetch latest task title for each employee.
    print("\n25. Subquery()")

    latest_task = (Task.objects.filter(assigned_to=OuterRef("pk")).order_by("-created_at"))

    employees = Employee.objects.annotate(
        latest_task=Subquery(latest_task.values("title")[:1]))

    for employee in employees[:5]:
        print(
            employee.name,
            employee.latest_task
        )

    # 26. OuterRef() 
    # Used inside Subquery to refer to outer Employee query.
    print("\n26. OuterRef()")

    print(
        "OuterRef('pk') refers to "
        "Employee primary key inside Subquery."
    )

    # 27. Exists()
    #What
    # — Boolean subquery: returns True/False per row depending on whether a related sub‐SELECT returns any rows.

    # When
    # — You want to annotate or filter based on the existence of related records.
    # Check if employee has pending tasks.
    print("\n27. Exists()")

    pending_tasks = Task.objects.filter(assigned_to=OuterRef("pk"),status="pending")

    employees = Employee.objects.annotate(has_pending=Exists(pending_tasks))

    for employee in employees[:5]:
        print(
            employee.name,
            f"Has Pending Tasks: {employee.has_pending}"
        )