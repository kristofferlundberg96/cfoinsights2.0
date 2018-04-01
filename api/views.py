from employees.models import Employee
from rest_framework import viewsets
from api.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer