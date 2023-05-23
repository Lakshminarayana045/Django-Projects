from django.db import models
class CoursesData(models.Model):
    course_name = models.CharField(max_length=30)
    course_fee = models.IntegerField()
    start_date = models.DateField()
    duration = models.CharField(max_length=30)
    trainer_name = models.CharField(max_length=30)
    trainer_exp = models.CharField(max_length=20)
