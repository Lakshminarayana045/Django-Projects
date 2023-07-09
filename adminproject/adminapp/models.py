from django.db import models

class EmpData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


