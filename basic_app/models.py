from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)