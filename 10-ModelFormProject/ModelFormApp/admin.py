from django.contrib import admin
from django.db import models
from ModelFormApp.models import StudentRegister

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

# Register your models here.
admin.site.register(StudentRegister,StudentAdmin)


