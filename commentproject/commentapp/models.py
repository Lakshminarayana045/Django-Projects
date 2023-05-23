from django.db import models


class CommentData(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateField()
