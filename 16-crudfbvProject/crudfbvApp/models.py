from django.db import models

# Create your models here.
class Employee(models.Model):
    enum=models.IntegerField()
    ename=models.CharField(max_length=60)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)