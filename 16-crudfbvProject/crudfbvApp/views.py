from django.shortcuts import render,redirect
from crudfbvApp.models import Employee
from crudfbvApp.forms import Employeeform

# Create your views here.
def retrieve_view(request):
    employees = Employee.objects.all()
    return render(request,'crudfbvApp/index.html',{'employees':employees})


def create_view(request):
    if request.method=='GET':
        form=Employeeform()
        return render(request,'crudfbvApp/create.html',{'form':form})
    elif request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid:
            form.save(commit=True)   ## ModelForm will directly Populate Model/Db
            return redirect('/')

def delete_view(request,id):
    employee=Employee.objects.get(id=id)   #id is the unique identifier of record in table added by Django
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=Employeeform(request.POST,instance=employee)   # Instance to be added so that same object of employee to be update if missing django will consider to add new employee record.
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'crudfbvApp/update.html',{'employee':employee})

  