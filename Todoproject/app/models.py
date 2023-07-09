from django.db import models

class userdata(models.Model):
    title=models.CharField(max_length=50)
    selectdata=models.DateField()
    taskdescription=models.CharField(max_length=200)
