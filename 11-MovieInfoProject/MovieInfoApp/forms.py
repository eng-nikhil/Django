from django import forms
from django.forms import fields
from MovieInfoApp.models import MovieInfoModel

class MovieInfoForm(forms.ModelForm):
    class Meta:
        model=MovieInfoModel
        fields='__all__'
        
