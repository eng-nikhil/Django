"""cbvProject_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cbvApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booklist/',views.BookListClass.as_view()),
    path('bookcustomlist/',views.BookListCustomizedClass.as_view(),name='booksdisplay'),
    path('bookdetail/<int:pk>',views.BookDetailClass.as_view(),name='detail'),  #Used name=detail so that revese of create view will call this using 'detail'(models.py)
    path('createbook/',views.BookCreatClass.as_view()),
    path('updatebook/<int:pk>',views.BookUpdateClass.as_view()),
    path('deletebook/<int:pk>',views.BookDeleteClass.as_view())
]

