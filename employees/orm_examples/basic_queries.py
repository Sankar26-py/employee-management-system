from django.db.models import Avg, Count
from employees.models import Employee, Department

def run():

    print("\n========== BASIC ORM QUERIES ==========")

    # 1. all() Returns all objects in the queryset.
    # Returns all records from the Employee table.
    print("\n1. all()")
    print(Employee.objects.all()[:5])

    # 2. filter() Filters data using keyword arguments.
    # Returns employees whose salary is greater than 100000.
    print("\n2. filter()")

    employees = Employee.objects.filter(salary__gt=100000)[:5]

    for emp in employees:
        print(emp.name, emp.salary)

    # 3. exclude() Excludes objects matching the condition.
    # Excludes inactive employees from the result.
    print("\n3. exclude()")

    print(Employee.objects.exclude(is_active=False).count())

    # 4. get() Returns exactly one object; throws error if zero or more than one
    # Returns a single employee matching the given condition.
    print("\n4. get()")

    try:
        employee = Employee.objects.get(id=1)
        print(employee.name)

    except Employee.DoesNotExist:
        print("Employee not found")

    # 5. order_by() Sorts the queryset.
    # Sorts employees by salary in descending order.
    print("\n5. order_by()")

    for emp in Employee.objects.order_by("-salary")[:5]:
        print(emp.name, emp.salary)

    # 6. values() Returns dictionaries of selected fields.s
    # Returns selected fields as dictionaries.
    print("\n6. values()")

    print(list( Employee.objects.values("id","name","salary")[:5]))

    # 7. values_list() Returns tuples of selected fields.
    # Returns selected fields as tuples or a flat list.
    print("\n7. values_list()")

    print(list(Employee.objects.values_list("name",flat=True)[:5]))

    # 8. annotate() Adds calculated fields to each object.
    # Adds employee_count to every department.
    print("\n8. annotate()")

    departments = Department.objects.annotate(employee_count=Count("employees"))

    for dept in departments:

        print(dept.name,dept.employee_count)

    # 9. aggregate() Performs calculation over entire queryset.
    # Calculates the average salary of all employees.
    print("\n9. aggregate()")

    print(Employee.objects.aggregate(avg_salary=Avg("salary")))

    # 10. distinct() Removes duplicates.
    # Removes duplicate department values.
    print("\n10. distinct()")

    print(list(Employee.objects.values("department").distinct()))

    # 11. exists()Checks if any records exist.
    # Checks whether employees with salary greater than 150000 exist.
    print("\n11. exists()")

    print(Employee.objects.filter(salary__gt=150000).exists())

    