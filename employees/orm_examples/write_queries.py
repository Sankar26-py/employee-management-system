from employees.models import Employee, Department
from tasks.models import Task
from datetime import date
from faker import Faker #type:ignore
import random
fake = Faker()
def run():


    print("\n========== WRITE QUERIES ==========")

    # 14. update() Bulk update of queryset.
    # Updates matching employee records directly in the database.
    print("\n14. update()")

    updated_count = Employee.objects.filter(salary__lt=50000).update(salary=50000)

    print(f"Updated Records: {updated_count}")

    # 15. delete() Deletes objects in the queryset.
    # Deletes all completed tasks from the database.
    print("\n15. delete()")

    deleted_count, _ = Task.objects.filter(status="completed").delete()

    print(f"Deleted Records: {deleted_count}")

    # 16. create() Creates and saves a new object
    # Creates and saves a new employee record.
    print("\n16. create()")
    
    employee = Employee.objects.create(
        name=fake.name(),
        email=fake.unique.email(),
        phone=fake.phone_number(),
        gender=random.choice(["male", "female"]),
        salary=random.randint(30000,200000),
        joining_date=fake.date_between(start_date="-5y",end_date="today"),
        department=Department.objects.first()
    )

    print(f"Created Employee: {employee.name}")

    # 17. bulk_create() Creates multiple objects at once.
    # Creates multiple employee records in a single database query.
    print("\n17. bulk_create()")

    employees = [
        Employee(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            gender=random.choice(["male", "female"]),
            salary=random.randint(30000,200000),
            joining_date=fake.date_between(start_date="-5y",end_date="today"),
            department=Department.objects.first()
            ),
        Employee(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            gender=random.choice(["male", "female"]),
            salary=random.randint(30000,200000),
            joining_date=fake.date_between(start_date="-5y",end_date="today"),
            department=Department.objects.first()
        )
    ]

    Employee.objects.bulk_create(employees)

    print("Created 2 Employees")

    # 18. in_bulk() Returns a dictionary keyed by IDs.
    # Returns a dictionary of employees keyed by their primary key.
    print("\n18. in_bulk()")

    employees_dict = Employee.objects.in_bulk([1, 2, 3])

    for emp_id, employee in employees_dict.items():

        print(
            emp_id,
            employee.name
        )

