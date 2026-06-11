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


# 22. Q()
# Allows OR, AND and NOT operations.
Employee.objects.filter(
    Q(salary__gt=100000) |
    Q(gender="female")
)


# 23. F()
# Compares fields at database level.
Task.objects.filter(
    completed_hours__lt=
    F("estimated_hours")
)


# 24. Case / When
# SQL CASE expression.
Employee.objects.annotate(
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


# 25. Subquery()
latest_task = (
    Task.objects
    .filter(
        assigned_to=OuterRef("pk")
    )
    .order_by("-created_at")
)

Employee.objects.annotate(
    latest_task=Subquery(
        latest_task.values("title")[:1]
    )
)


# 26. OuterRef()
OuterRef("pk")


# 27. Exists()
pending_tasks = Task.objects.filter(
    assigned_to=OuterRef("pk"),
    status="pending"
)

Employee.objects.annotate(
    has_pending=Exists(
        pending_tasks
    )
)