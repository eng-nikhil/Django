from django import forms
from django.forms import fields
from crudfbvApp.models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'