from django.db import models

class StudentData(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    coursename=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    hometown=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    percentage=models.IntegerField()
    passedoutyear=models.IntegerField()
