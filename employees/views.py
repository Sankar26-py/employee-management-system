from django.db.models import Avg
from django.db.models import Count

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Department, Employee
from .serializers import DepartmentSerializer,EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.annotate(employee_count=Count("employees"))
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.select_related("department")
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=["get"])
    def high_salary(self, request):

        queryset = Employee.objects.filter(salary__gte=100000)
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def top_performers(self, request):

        queryset = Employee.objects.filter(employeeproject__rating__gte=4.5).distinct()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def salary_stats(self, request):

        data = Employee.objects.aggregate(average_salary=Avg("salary"))
        return Response(data)