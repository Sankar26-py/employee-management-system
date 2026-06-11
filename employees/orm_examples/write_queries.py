from employees.models import Employee, Department
from tasks.models import Task


# 14. update()
# Updates matching rows directly in DB.
Employee.objects.filter(
    salary__lt=50000
).update(
    salary=50000
)


# 15. delete()
# Deletes matching rows immediately.
Task.objects.filter(
    status="completed"
).delete()


# 16. create()
# Creates and saves a new employee.
Employee.objects.create(
    name="Test User",
    email="test@test.com",
    gender="male",
    salary=75000,
    department=Department.objects.first()
)


# 17. bulk_create()
employees = [
    Employee(
        name="User1",
        email="user1@test.com",
        gender="male",
        salary=60000,
        department=Department.objects.first()
    ),
    Employee(
        name="User2",
        email="user2@test.com",
        gender="female",
        salary=65000,
        department=Department.objects.first()
    )
]

Employee.objects.bulk_create(
    employees
)


# 18. in_bulk()
# Returns dictionary keyed by id.
Employee.objects.in_bulk(
    [1, 2, 3]
)