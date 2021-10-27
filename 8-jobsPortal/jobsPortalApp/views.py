from django.shortcuts import render
from jobsPortalApp.models import delhijobs as v1
from jobsPortalApp.models import bangalorejobs as v2
from jobsPortalApp.models import punejobs as v3


# Create your views here.

def index(request):
    return render(request,'jobsPortalApp/index.html')
   

def bangalorejobs(request): 
    bangalorejobs_list=v2.objects.all()
    jobs_dict={'location':'Bangalore','jobs_list':bangalorejobs_list}

    return render(request,'jobsPortalApp/jobsinfopage.html',context=jobs_dict)

def delhijobs(request):
    delhijobs_list=v1.objects.order_by('date')
    jobs_dict={'location':'Delhi','jobs_list':delhijobs_list}
    return render(request,'jobsPortalApp/jobsinfopage.html',context=jobs_dict)

def punejobs(request):
    punejobs_list=v3.objects.all()
    jobs_dict={'location':'Pune','jobs_list':punejobs_list}
    return render(request,'jobsPortalApp/jobsinfopage.html',context=jobs_dict)