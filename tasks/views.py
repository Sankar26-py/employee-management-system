from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

from django.db.models import F

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.select_related("project","assigned_to")
    serializer_class = TaskSerializer

    @action(detail=False, methods=["get"])
    def pending_tasks(self, request):

        queryset = Task.objects.filter(status="pending")
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def incomplete_tasks(self, request):

        queryset = Task.objects.filter(completed_hours__lt=F("estimated_hours"))
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)