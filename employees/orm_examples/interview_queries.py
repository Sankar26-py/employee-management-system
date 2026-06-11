from django.db.models import Avg, Count

from employees.models import Employee, Department
from projects.models import Project


# Top 5 Highest Paid Employees
Employee.objects.order_by("-salary")[:5]


# Department Wise Employee Count
Department.objects.annotate(
    employee_count=Count("employees")
)


# Employees With Pending Tasks
Employee.objects.filter(
    tasks__status="pending"
).distinct()


# Projects With More Than 10 Tasks
Project.objects.annotate(
    task_count=Count("tasks")
).filter(
    task_count__gt=10
)


# Average Salary Per Department
Department.objects.annotate(
    avg_salary=Avg(
        "employees__salary"
    )
)


# Highest Rated Employee
Employee.objects.annotate(
    avg_rating=Avg(
        "employeeproject__rating"
    )
).order_by(
    "-avg_rating"
).first()