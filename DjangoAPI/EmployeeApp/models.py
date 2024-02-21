from django.db import models

# Create your models here.

# To store department details
class Departments(models.Model):
    # To store automated incremented department id
    DepartmentId = models.AutoField(primary_key=True)
    # to store department name
    DepartmentName = models.CharField(max_length=500)

# to store employee details
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
