from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from cbvApp.models import Book


# Create your views here.

### Function Based View #####
def info_view(request):
    books=Book.objects.all()
    return render(request,'cbvApp/info.html',{'books':books})


### Class Based List  View  Using Deault Template #####
class BookListClass(ListView):
    model=Book
   #Default Template: book_list.html
   #Default Context Object: book_list



### Class Based List View  Using Customized Template and context #####
class BookListCustomizedClass(ListView):
    model=Book
    template_name="cbvApp/customised_book_list.html"    # 'template_name' is Django defined  variable name
    context_object_name='list_of_books'                 # 'context_object_name' is Django defined  variable name
                                                        # Even one of template_name, context_object_name can be used
                                                        # not neccessary to use both 


### Class Based Detail View  Using Deault Template #####
class BookDetailClass(DetailView):
    model=Book
   #Default Template: book_detail.html
   #Default Context Object: book 


### Class Based Create View Using Deault Template #####
class BookCreatClass(CreateView):
    model=Book                                      
    fields=('title','author','pages','price')
    #Default Template: book_form.html
    #Default Context Object: book 
    # After Successful Insertion next page will be loaded as defined in func get_absolute_url in models.py  

### Class Based Update View Using Deault Template #####
class BookUpdateClass(UpdateView):
    model=Book
    fields=('pages','price')   # Fields which can be updated
    #Default Template: book_form.html  **********It will use Same Default form as Create *********
    #Default Context Object: book 
    # After Successful update next page will be loaded as defined in func get_absolute_url in models.py


### Class Based Delete View Using Deault Template #####

class BookDeleteClass(DeleteView):
    model=Book
    success_url=reverse_lazy('booksdisplay')
    #Default Template: book_confirm_delete.html

    # Before deletion control will go to 'book_confirm_Delete.html' for confirmation
    #book_confirm_Delete should 'Submit' a Post method for successful deletion

    # After Successful Deletion next page will be loaded as defined in reverese_lazy method 
    # success_url is fixed keyword of Django 
    # booksdisplay -> is defined in urls for bookcustomlist/
    