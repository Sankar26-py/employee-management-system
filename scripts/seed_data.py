import os
import sys
import django
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","employee_management_system.settings")
django.setup()

from faker import Faker # type: ignore
from employees.models import Employee,Department
from projects.models import Project,EmployeeProject
from tasks.models import Task

fake = Faker()

def create_departments():

    departments = ["IT","HR","Finance","Operations","Sales","Marketing"]

    department_objects = []

    for dept in departments:
        department = Department.objects.create(
            name=dept,
            budget=random.randint(
                500000,
                5000000
            )
        )

        department_objects.append(department)

    return department_objects

def create_employees(departments):

    employees = []

    for _ in range(200):

        employee = Employee(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            gender=random.choice(["male", "female"]),
            salary=random.randint(30000,200000),
            joining_date=fake.date_between(start_date="-5y",end_date="today"),
            department=random.choice(departments),
            is_active=random.choice([True, True, True, False])
        )

        employees.append(employee)

    Employee.objects.bulk_create(employees)

    return list(Employee.objects.all())

def create_projects():

    projects = []

    statuses = ["planned","active","completed"]

    for i in range(50):

        project = Project(
            name=f"Project {i+1}",
            description=fake.text(),
            budget=random.randint(100000,2000000),
            status=random.choice(statuses),
            start_date=fake.date_between("-2y","today"),
            metadata={"priority":random.choice(["low","medium","high"])}
        )

        projects.append(project)

    Project.objects.bulk_create(projects)

    return list(Project.objects.all())

def create_employee_projects(employees,projects):

    mappings = []

    for project in projects:

        selected_employees = random.sample(employees,random.randint(3,10))

        for employee in selected_employees:

            mappings.append(
                EmployeeProject(
                    employee=employee,
                    project=project,
                    hours_allocated=random.randint(50,500),
                    rating=round(random.uniform(1,5),2)
                )
            )

    EmployeeProject.objects.bulk_create(mappings)

def create_tasks(employees,projects):

    tasks = []

    statuses = ["pending","in_progress","completed"]

    priorities = ["low","medium","high"]

    for _ in range(1000):

        tasks.append(
            Task(
                title=fake.sentence(),
                description=fake.text(),
                project=random.choice(projects),
                assigned_to=random.choice(employees),
                status=random.choice(statuses),
                priority=random.choice(priorities),
                estimated_hours=random.randint(1,100),
                completed_hours=random.randint(0,100)
            )
        )

    Task.objects.bulk_create(tasks)

def seed():

    print("Creating departments...")

    departments = create_departments()

    print("Creating employees...")

    employees = create_employees(departments)

    print("Creating projects...")

    projects = create_projects()

    print("Creating mappings...")

    create_employee_projects(employees,projects)

    print("Creating tasks...")

    create_tasks(employees,projects)

    print("Done")

if __name__ == "__main__":
    seed()