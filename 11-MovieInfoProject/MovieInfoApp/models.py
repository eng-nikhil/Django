from django.db import models
from django.db.models.base import Model
from django.db import models

# Create your models here.
class MovieInfoModel(models.Model):
    name=models.CharField(max_length=50)
    rdate=models.DateField(auto_now=True)
    actor=models.CharField(max_length=50)
    actoress=models.CharField(max_length=50)
    rating=models.IntegerField()
    

