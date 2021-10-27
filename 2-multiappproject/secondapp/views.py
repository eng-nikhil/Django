from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish2(request):
    msg = "<h1>This is Second App</h1>"
    return HttpResponse(msg)