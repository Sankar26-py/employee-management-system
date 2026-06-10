from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    employee_name = serializers.CharField(source="assigned_to.name",read_only=True)
    project_name = serializers.CharField(source="project.name",read_only=True)

    class Meta:
        model = Task
        fields = "__all__"