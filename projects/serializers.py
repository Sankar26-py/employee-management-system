from rest_framework import serializers
from .models import Project, EmployeeProject


class EmployeeProjectSerializer(serializers.ModelSerializer):

    employee_name = serializers.CharField(source="employee.name",read_only=True)
    project_name = serializers.CharField(source="project.name",read_only=True)

    class Meta:
        model = EmployeeProject
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    employee_count = serializers.IntegerField(read_only=True)
    task_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"