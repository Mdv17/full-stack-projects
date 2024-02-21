# Serializers help to convert the complex types of model instances into native python data types that can easily be rendered to JSON, or XML or other content types
# They also help in deserializing which is converting the past data to complex types
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'