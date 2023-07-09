from django.db import models

class student(models.Model):
    Name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    dob=models.DateField()
    marks_percentage=models.IntegerField()
    class_group=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
