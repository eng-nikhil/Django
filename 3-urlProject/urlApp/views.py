from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
    s='<h1> HYderabad Jobs Info'
    return HttpResponse(s)

def punejobs(request):
    s='<h1> Pune Jobs Info'
    return HttpResponse(s)

def delhijobs(request):
    s='<h1> Delhi Jobs Info'
    return HttpResponse(s)
