from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish1(request):
    msg = "<h1>This is First App</h1>"
    return HttpResponse(msg)
