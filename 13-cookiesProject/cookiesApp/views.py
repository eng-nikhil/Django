from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=int(request.COOKIES.get('count',0))  # return count value if not found send 0.
    new_count=count+1

    
    respose= render(request,'cookiesApp/count.html',{'count':new_count})  
    
     ### Temporay Cookies: will be stored in client's Browser Cache #####
    respose.set_cookie('count',new_count)   # keep this cookie for 3 minutes
    ### Persistant Cookies: will be stored in client's Persistent memory for Given time i.e max_age(in sec) ### 
    respose.set_cookie('count',new_count,max_age=180)   # keep this cookie for 3 minutes
    return respose


