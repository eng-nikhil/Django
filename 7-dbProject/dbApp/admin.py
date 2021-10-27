from django.contrib import admin
from dbApp.models import Employee

# To show coloumns on the admin gui
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)

#Employee-> to get data
#EmployeeAdmin-> to show particular coloumns as per above list
