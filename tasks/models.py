from django.db import models
from employees.models import Employee
from projects.models import Project
from .managers import TaskManager

class Task(models.Model):

    STATUS_CHOICES = (("pending", "Pending"),("in_progress", "In Progress"),("completed", "Completed"),)    
    PRIORITY_CHOICES = (("low", "Low"),("medium", "Medium"),("high", "High"),)
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
    assigned_to = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="tasks")
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default="medium")
    estimated_hours = models.PositiveIntegerField()
    completed_hours = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskManager()
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title