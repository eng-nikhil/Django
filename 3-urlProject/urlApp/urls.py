from django.urls import path
from urlApp import views

urlpatterns = [
    path('hydjobs/', views.hydjobs),
    path('punejobs/', views.punejobs),
    path('delhijobs/', views.delhijobs),
]