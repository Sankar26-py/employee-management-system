from employees.models import Employee
from projects.models import Project


def run():

    print("\n========== QUERY OPTIMIZATION ==========")

    # 12. select_related() Joins related models in a single query (for ForeignKey/OneToOne).
    # Fetches department data using SQL JOIN in a single query.
    print("\n12. select_related()")

    employees = Employee.objects.select_related("department")

    for employee in employees[:5]:
        print(f"{employee.name} -> "f"{employee.department.name}")

    # 13. prefetch_related() Pre-fetches related objects (for reverse/many-to-many).
    # Fetches tasks and employees using separate optimized queries.
    print("\n13. prefetch_related()")

    projects = Project.objects.prefetch_related("tasks","employees")

    for project in projects[:3]:
        print(f"{project.name} | "f"Tasks: {project.tasks.count()} | "f"Employees: {project.employees.count()}")

    # 20. defer() Loads only specified fields or defers loading of some.
    # Delays loading email field until accessed.
    print("\n20. defer()")

    employees = Employee.objects.defer("email")

    for employee in employees[:5]:
        print(f"Name: {employee.name}, "f"Salary: {employee.salary}")

    # Accessing email triggers an extra query
    print("\nAccessing deferred field:")
    employee = employees.first()

    print(f"{employee.name} -> "f"{employee.email}")

    # 21. only() loads only specified fields
    # Loads only specified fields initially.
    print("\n21. only()")

    employees = Employee.objects.only("name","salary")

    for employee in employees[:5]:
        print(f"Name: {employee.name}, "f"Salary: {employee.salary}")

    # Accessing a non-selected field triggers an additional query.
    print("\nAccessing non-selected field:")
    employee = employees.first()

    print(f"{employee.name} -> "f"{employee.email}")