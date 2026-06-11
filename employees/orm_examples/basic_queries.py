from django.db.models import Avg, Count

from employees.models import Employee, Department


# 1. all()
# Returns all records from the Employee table.
Employee.objects.all()


# 2. filter()
# Returns employees whose salary is greater than 100000.
Employee.objects.filter(salary__gt=100000)


# 3. exclude()
# Excludes inactive employees.
Employee.objects.exclude(is_active=False)


# 4. get()
# Returns a single employee.
# Raises DoesNotExist or MultipleObjectsReturned.
Employee.objects.get(id=1)


# 5. order_by()
# Sorts employees by salary descending.
Employee.objects.order_by("-salary")


# 6. values()
# Returns dictionaries instead of model instances.
Employee.objects.values("id", "name", "salary")


# 7. values_list()
# Returns tuples or a flat list when flat=True.
Employee.objects.values_list("name", flat=True)


# 8. annotate()
# Adds employee_count to every department.
Department.objects.annotate(
    employee_count=Count("employees")
)


# 9. aggregate()
# Calculates average salary across all employees.
Employee.objects.aggregate(
    avg_salary=Avg("salary")
)


# 10. distinct()
# Removes duplicate department ids.
Employee.objects.values(
    "department"
).distinct()


# 11. exists()
# Returns True if matching records exist.
Employee.objects.filter(
    salary__gt=150000
).exists()