from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView    # to make Class Based Views

# Create your views here.

class HelloWorldClass(View):        # Not Using Templates
    def get(self,request):
        return HttpResponse('<h1>This is Class Based View</h1>')


class HelloWorldTemplateClass(TemplateView):   # To use Templates, pass Template view 
    template_name='cbvApp/welcome.html'

class HelloWorldTemplateContext(TemplateView):   # To use Templates, pass Template view 
    template_name='cbvApp/info.html'
    def get_context_data(self, **kwargs):   # **kwargs(key-word Arguments) -> Dict[str, Any] and number of key-value can be passed
                                            # Any variable can be used in place of kwargs with ** for eg: **var1 
        context= super().get_context_data(**kwargs)   # Calling Parent class method get_context_data
        context['name']='Nikhil'
        context['subject']='Python'
        context['marks']=100
        return context
