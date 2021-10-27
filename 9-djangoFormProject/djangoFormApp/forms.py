from django import forms

from django.core import validators  # For Implicit Valication

################# METHOD - 1 ( Independent Functions) ##########################
# Explicit Validations to be called explicitity  outside of Class   
# Can be defined in other file like validations.py and can be imported that file  
#Recommended Approach

def starts_with_d(value):
    if value[0]!='d':
        raise forms.ValidationError("Name not starts with 'd'")

def gmail_domain_check(value):
    if value[len(value)-9::] !='gmail.com':
        raise forms.ValidationError('Invalid Email Domain expected is gmail.com')

def alphabet_check(value):
    if value.isalpha()== False:
        raise forms.ValidationError('Numberic Values not allowed')


#################################################################


# Form Class
class Studentregister(forms.Form):
    name=forms.CharField(validators=[starts_with_d,alphabet_check],label='Name')
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_domain_check])
    remarks=forms.CharField(label = 'Student Remarks',widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])  ## Implicit Validators
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)  # Hidden Field to identify whether request sent by BOT


################## METHOD-2 ( Class Impllict Consturvtor/Method) #############################
## Explicit Validation Methods syntax: clean_fieldname(self) - Methods of Class##
# if validation name is in format clean_fieldname(self)  it will be called automatically
# Explicity valications with Implicit calls like constructor
# To be defined inside the class
    def clean_name(self):
        inputname=self.cleaned_data['name']
        print('..........',inputname)
        if len(inputname)<4:
            raise forms.ValidationError('Length of Name should be more than 4 chars')
        return inputname   

    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('Email Validation')        
        return inputemail       

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        return inputrollno  
################################################################################


############## METHOD-3 (Complete form Validation using implicit clean method-Auto call) ######
### Good Approach if we want to compare whether two values are matching for eg: Password and renter-password fields

    def clean(self):
        print('Total Form Validation')
        cleaned_data= super().clean()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError("Thanks..BOT")

        inputname=cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Length of Name should be More than 4")

        inputroll=cleaned_data['rollno']
        if len(str(inputroll))<3:
            raise forms.ValidationError("Length of rollno should be More than 3")

        inputemail=cleaned_data['email']
        if inputemail[len(inputemail)-9::] !='gmail.com':
            raise forms.ValidationError('Invalid Email Domain expected is gmail.com')
