from django.shortcuts import render
from djangoFormApp import forms
from django.core.exceptions import ValidationError

# Create your views here.
def studentregistration(request):
    if request.method=='GET':
        form = forms.Studentregister()
        return render(request,'djangoFormApp/register.html',{'form':form})
    if request.method=='POST':
        form=forms.Studentregister(request.POST)
       # print('.....',request.POST)
        if form.is_valid():
            print('Form Validation  Success,Getting Student Data as:')
            print('Student Name:',form.cleaned_data['name'])
            print('Student RollNo:',form.cleaned_data['rollno'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student Remarks:',form.cleaned_data['name'])
            return render(request,'djangoFormApp/thanks.html',{'name':form.cleaned_data['name']})
        return render(request,'djangoFormApp/register.html',{'form':form})

       
    



