from django.db import models
from django.utils import timezone


class EmployeeQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)

    def high_salary(self):
        return self.filter(salary__gte=100000)

    def low_salary(self):
        return self.filter(salary__lt=50000)

    def joined_this_year(self):
        return self.filter(joining_date__year=timezone.now().year)

    def by_department(self, department_name):
        return self.filter(department__name=department_name)


class EmployeeManager(models.Manager):

    def get_queryset(self):
        return EmployeeQuerySet(self.model,using=self._db)

    def active(self):
        return self.get_queryset().active()

    def high_salary(self):
        return self.get_queryset().high_salary()

    def joined_this_year(self):
        return self.get_queryset().joined_this_year()