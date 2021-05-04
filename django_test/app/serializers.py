from .models import *
from rest_framework import serializers

class EmployeesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employees
		fields='__all__'
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model=Company_Staff
		fields='__all__'
class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model=People
		fields='__all__'
		
		
			
	"""docstring for EmployeesSerializers"""
	
