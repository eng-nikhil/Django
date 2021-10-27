from django.contrib import admin
from django.contrib.admin.sites import site
from cbvApp.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']


admin.site.register(Book,BookAdmin)



