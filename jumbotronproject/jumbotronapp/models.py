from django.db import models

class studentsdata(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    qualification=models.CharField(max_length=50)
    passoutyear=models.IntegerField()

























'''


class EmployeeData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=150)
    company=models.CharField(max_length=50)
    salary=models.BigIntegerField()
    location=models.CharField(max_length=100)
'''
