from django.db.models import Avg, Count

from employees.models import Employee, Department
from projects.models import Project

from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

def run():

    print("\n========== REAL WORLD ORM EXAMPLES ==========")

    # Top 5 Highest Paid Employees
    print("\n1. Top 5 Highest Paid Employees")

    employees = (Employee.objects.order_by("-salary")[:5])

    for employee in employees:

        print(employee.name,employee.salary)

    # Department Wise Employee Count
    print("\n2. Department Wise Employee Count")

    departments = (Department.objects.annotate(employee_count=Count("employees")))

    for department in departments:

        print(department.name,department.employee_count)

    # Employees With Pending Tasks
    print("\n3. Employees With Pending Tasks")

    employees = (Employee.objects.filter(tasks__status="pending").distinct())

    for employee in employees:

        print(employee.name)

    # Projects With More Than 10 Tasks
    print("\n4. Projects With More Than 10 Tasks")

    projects = (Project.objects.annotate(
        task_count=Count("tasks")).filter(task_count__gt=10))

    for project in projects:

        print(project.name,project.task_count)

    # Average Salary Per Department
    print("\n5. Average Salary Per Department")

    departments = (Department.objects.annotate(avg_salary=Avg("employees__salary")))

    for department in departments:

        print(department.name,round(department.avg_salary or 0,2))

    # Highest Rated Employee
    print("\n6. Highest Rated Employee")

    employee = (
        Employee.objects
        .annotate(avg_rating=Avg("employeeproject__rating"))
        .order_by("-avg_rating")
        .first()
    )

    if employee:
        print( employee.name,employee.avg_rating)

    print("\n========== get_object_or_404() ==========") #Django shortcut for views
    #is a Django shortcut used to retrieve a single object. If the object doesn't exist, 
    # it automatically raises an HTTP 404 error instead of a DoesNotExist exception.

    try:

        employee = get_object_or_404(Employee,id=1)
        print(employee.name,employee.salary)

    except Exception as e:
        print(e)


    print("\n========== get_list_or_404() ==========")

    try:

        employees = get_list_or_404(Employee,department_id=1)
        print(employee.name,employee.salary)

    except Exception as e:
        print(e)
