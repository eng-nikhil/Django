from django.shortcuts import render
import datetime

# Create your views here.
def tempview(request):
    return render(request,'testApp/wish.html')

def dynamicview(request):
    date=datetime.datetime.now()
    my_dict= {'date_msg':date}
    return render(request,'testApp/dynamicwish.html',context=my_dict)