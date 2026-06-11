from employees.models import Employee
from projects.models import Project


# 12. select_related()
# Performs SQL JOIN and fetches department data
# in the same query.
Employee.objects.select_related(
    "department"
)


# 13. prefetch_related()
# Fetches related tasks and employees using
# separate optimized queries.
Project.objects.prefetch_related(
    "tasks",
    "employees"
)


# 20. defer()
# Delays loading email field until accessed.
Employee.objects.defer("email")


# 21. only()
# Loads only name and salary initially.
Employee.objects.only(
    "name",
    "salary"
)