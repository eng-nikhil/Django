from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def homepage(request):
    return render(request,'MovieInfoApp/homepage.html')


def addmovie(request):
    if request.method=='GET':
        form = forms.MovieInfoForm()
        return render(request,'MovieInfoApp/Addmovie.html',context={'form':form})
    elif request.method=='POST':
        form=forms.MovieInfoForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
        return render(request,'MovieInfoApp/homepage.html')


def listmovie(request):
    movie_list = models.MovieInfoModel.objects.all()
    return render(request,'MovieInfoApp/viewmovie.html',context={'movie_list':movie_list})

