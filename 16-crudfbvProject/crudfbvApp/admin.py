from django.contrib import admin
from crudfbvApp.models import Employee

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['enum','ename','esal','eaddr']

admin.site.register(Employee,EmpAdmin)
