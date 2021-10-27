from django.shortcuts import render
from . import forms
# Create your views here.

def student_view(request):
    if request.method=='GET':
        form=forms.StudentForm()
        return render(request,'ModelFormApp/register.html',{'form':form})
    elif request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid:
            form.save(commit=True)   ## ModelForm will directly Populate Model/Db
        return render(request,'ModelFormApp/Thanks.html')