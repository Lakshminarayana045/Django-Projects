from django.db import models

class StudentsData(models.Model):
    first_name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    gmail = models.EmailField(max_length=100)
    location = models.CharField(max_length=50)
