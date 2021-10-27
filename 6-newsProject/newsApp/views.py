from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def sportsinfo(request):
    my_dict=newsfiller('sports')
    return render(request,'newsApp/news.html',context=my_dict)

def moviesinfo(request):
    my_dict=newsfiller('movies')
    return render(request,'newsApp/news.html',context=my_dict)

def politicsinfo(request):
    my_dict=newsfiller('politics')
    return render(request,'newsApp/news.html',context=my_dict)

def newsfiller(newstype):
    temp_dict=[]
    if newstype=='sports':
        news_type='Sports'
        msg_1='Sports News-1'
        msg_2='Sports News-2'
        msg_3='Sports News-3'
        msg_4='Sports News-4'
    elif newstype=='movies':
        news_type='Movies'
        msg_1='Movies News-1'
        msg_2='Movies News-2'
        msg_3='Movies News-3'
        msg_4='Movies News-4'
    else:
        news_type='Politics'
        msg_1='Politics News-1'
        msg_2='Politics News-2'
        msg_3='Politics News-3'
        msg_4='Politics News-4'
    temp_dict={'news_type':news_type,'msg_1':msg_1,'msg_2':msg_2,'msg_3':msg_3,'msg_4':msg_4}
    return temp_dict