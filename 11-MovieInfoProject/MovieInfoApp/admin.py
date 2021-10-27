from django.contrib import admin
from django.db import models
from MovieInfoApp.models import MovieInfoModel

class MovieModelAdmin(admin.ModelAdmin):
    list_display=['name','rdate','actor','actoress','rating']

# Register your models here.
admin.site.register(MovieInfoModel,MovieModelAdmin)  ##Name of Model, Fields to Displayed on Admin Site




