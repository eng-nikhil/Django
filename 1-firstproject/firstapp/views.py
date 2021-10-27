from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    s='<h1>First Django Project App</h1>'
    return HttpResponse(s)

def showtime(request):
    time= datetime.datetime.now()
    h=int(time.strftime("%H"))
    msg = "<h1 style=color:blue> Hi,"
    if h<12:
       msg+='Good Morning'
    elif h<16:
        msg+='Good Afternoon'
    elif h<21:
        msg+="Good Evening"
    else:
        msg+='Good Night' 
    msg+='<hr> Current time is: '+str(time)+'</h1>'
    return HttpResponse(msg)


    