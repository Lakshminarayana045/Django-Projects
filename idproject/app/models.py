from django.db import models

class EmployeeData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)
    salary = models.BigIntegerField()
    company = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    locations = models.CharField(max_length=50)
