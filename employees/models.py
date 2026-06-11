from django.db import models
from .managers import EmployeeQuerySet
from .managers import EmployeeManager


class Department(models.Model):

    name = models.CharField(max_length=100,unique=True)
    budget = models.DecimalField(max_digits=12,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(models.Model):

    GENDER_CHOICES = (("male", "Male"),("female", "Female"),)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25,blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name