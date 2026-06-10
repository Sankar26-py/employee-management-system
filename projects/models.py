from django.db import models
from employees.models import Employee


class Project(models.Model):

    STATUS_CHOICES = (("planned", "Planned"),("active", "Active"),("completed", "Completed"),)
    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=12,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="planned")
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    metadata = models.JSONField(default=dict,blank=True)
    employees = models.ManyToManyField(Employee,through="EmployeeProject",related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class EmployeeProject(models.Model):

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    hours_allocated = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    assigned_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("employee","project")

    def __str__(self):
        return (f"{self.employee.name} - "f"{self.project.name}")