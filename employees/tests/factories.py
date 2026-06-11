import factory #type: ignore
from datetime import date

from employees.models import Employee, Department


class DepartmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Department

    name = factory.Sequence(lambda n: f"Department-{n}")
    budget = 1000000


class EmployeeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Employee

    name = factory.Faker("name")
    email = factory.Sequence(lambda n: f"user{n}@test.com")
    phone = factory.Sequence(lambda n: f"987654{n:04d}")

    gender = "male"
    salary = 100000
    joining_date = date(2024, 1, 1)

    department = factory.SubFactory(
        DepartmentFactory
    )