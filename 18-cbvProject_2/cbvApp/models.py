from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.CharField(max_length=50)
    pages=models.PositiveIntegerField()
    price=models.FloatField()
    ## Used for Create view 
    #When a new instance(book) is created or Updated(existing) for a model, django will open the url given in get_absoulte_url method
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

