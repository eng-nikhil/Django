from django.contrib import admin
from jobsPortalApp.models import delhijobs
from jobsPortalApp.models import bangalorejobs
from jobsPortalApp.models import punejobs

# Register your models here.


# To show coloumns on the admin gui
class delhijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class banaglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

# Register your models here.
admin.site.register(delhijobs,delhijobsAdmin)
admin.site.register(bangalorejobs,banaglorejobsAdmin)
admin.site.register(punejobs,punejobsAdmin)

#Employee-> to get data
#EmployeeAdmin-> to show particular coloumns as per above list

