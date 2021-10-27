from django.shortcuts import render
from dbApp.models import Employee
from django.http import HttpResponse

# Create your views here.

def empview(request):
    emp_list=Employee.objects.all()
    emp_dict={"emp_list":emp_list}
    return render(request,'dbApp/empdetails.html',context=emp_dict)