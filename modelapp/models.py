from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(default=80)
    index_number = models.CharField(default=80)
    age = models.IntegerField()
    fess = models.IntegerField()