from django import forms
from ModelFormApp.models import StudentRegister

class StudentForm(forms.ModelForm):
   
    class Meta:
        model = StudentRegister
        fields = '__all__'
