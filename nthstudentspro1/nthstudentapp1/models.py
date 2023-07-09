from django.db import models

class mainpage(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    coursename=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    hometown=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    percentage=models.IntegerField()
    passedoutyear=models.IntegerField()
