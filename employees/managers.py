from django.db import models
from django.utils import timezone

class EmployeeQuerySet(models.QuerySet):

    def high_salary(self):
        return self.filter(salary__gte=100000)

    def low_salary(self):
        return self.filter(salary__lt=50000)

    def joined_this_year(self):
        
        return self.filter(joining_date__year=timezone.now().year)