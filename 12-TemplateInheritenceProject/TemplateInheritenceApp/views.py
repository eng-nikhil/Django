from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,'TemplateInheritenceApp/home.html')

def sportsview(request):
    return render(request,'TemplateInheritenceApp/sports.html')

def moviesview(request):
    return render(request,'TemplateInheritenceApp/movies.html')

def politicsview(request):
    return render(request,'TemplateInheritenceApp/politics.html')