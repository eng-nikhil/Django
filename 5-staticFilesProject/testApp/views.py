from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'testApp/home.html')

def welcome(request):
    return render(request,'testApp/welcome.html')