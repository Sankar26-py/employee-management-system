from employees.models import Employee,Department
from faker import Faker  #type:ignore
import random

fake = Faker()

def run():

    print("\n========== RETRIEVAL & UTILITY METHODS ==========")

    # 35. reverse() 
    # What
    #Reverses the ordering of a queryset (i.e. flips order_by()).
    #When
    #You’ve already applied an order_by() but want the opposite direction, without re‑typing all your fields.
    # Reverses the current ordering.
    print("\n35. reverse()")

    employees = (Employee.objects.order_by("salary").reverse())

    for employee in employees[:5]:

        print(employee.name,employee.salary)

    # 36. earliest() Shortcut for getting the single object with the minimum (earliest) 
    print("\n36. earliest()")

    try:

        employee = Employee.objects.earliest("joining_date")

        print(employee.name,employee.joining_date)

    except Employee.DoesNotExist:

        print("No employees found")

    # 37. latest() maximum (latest) value in a date‑ or orderable field.
    print("\n37. latest()")

    try:

        employee = Employee.objects.latest("joining_date")

        print(employee.name,employee.joining_date)

    except Employee.DoesNotExist:

        print("No employees found")

    # 38. first() Returns the first object in the queryset, or None if empty.
    print("\n38. first()")

    employee = Employee.objects.first()

    if employee:

        print(employee.name,employee.salary)

    # 39. last()  Returns the last object in the queryset, or None if empty.
    print("\n39. last()")

    employee = Employee.objects.last()

    if employee:

        print(employee.name,employee.salary)

    # 40. count() Returns an integer count of rows in the queryset.
    # Returns total number of records.
    print("\n40. count()")

    total = Employee.objects.count()

    print(f"Total Employees: {total}")

    # 41. get_or_create()
    # Gets existing record or creates one.
    print("\n41. get_or_create()")

    employee, created = (
        Employee.objects.get_or_create(
            email=fake.unique.email(),
            defaults={
                "name": fake.name(),
                "gender": random.choice(["male", "female"]),
                "salary": random.randint(55000,110000),
                "joining_date":fake.date_between(start_date="-5y",end_date="today"),
                "department":Department.objects.first()
            }
        )
    )

    print(f"Employee: {employee.name}")
    print(f"Created: {created}")

    # 42. update_or_create()
    # Updates existing record or creates new one.
    print("\n42. update_or_create()")

    employee, created = (
        Employee.objects.update_or_create(
            email=fake.unique.email(),
            defaults={
                "salary": 90000,
                "joining_date":fake.date_between(start_date="-5y",end_date="today"),
                "department":Department.objects.first()
            }
        )
    )

    print(f"Employee: {employee.name}")
    print(f"Salary: {employee.salary}")
    print(f"Created: {created}")