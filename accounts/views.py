from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee 
from .serializers import EmployeeSerializer

class EmployeeViewset(viewsets.ModelViewSet):
	queryset=Employee.objects.none()
	serializer_class=EmployeeSerializer



@api_view(['GET'])
def get_data(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many = True)
    return Response(serializer.data)



"""
@api_view(['GET', ])
def api_detail_employee_view(request):
	try:
		queryset=Employee.objects.all()
	except Employee.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =="GET":
		serializer = EmployeeSerializer(queryset)
		return Response(serializer.data)
"""

