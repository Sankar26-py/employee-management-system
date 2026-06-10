from django.db.models import Count

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project, EmployeeProject
from .serializers import ProjectSerializer,EmployeeProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.prefetch_related("tasks","employees").annotate(
        task_count=Count("tasks"),
        employee_count=Count("employees")
        )
    serializer_class = ProjectSerializer

    @action(detail=False, methods=["get"])
    def active_projects(self, request):

        queryset = Project.objects.filter(status="active")
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def project_summary(self, request):

        total_projects = Project.objects.count()
        active_projects = Project.objects.filter(status="active").count()
        completed_projects = Project.objects.filter(status="completed").count()

        return Response({
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects
        })
    
class EmployeeProjectViewSet(viewsets.ModelViewSet):

    queryset = EmployeeProject.objects.select_related("employee","project")
    serializer_class = EmployeeProjectSerializer