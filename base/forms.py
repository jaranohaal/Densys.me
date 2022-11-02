#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
DATE_INPUT_FORMATS = ['%d.%m.%Y']

def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

def is_blood_group(value):
    if value != 'O' or value != 'A' or value != 'B' or value != 'AB':
        raise ValidationError('incorrect blood group')
BLOOD_GROUPS = ['O','A','B','AB']
class RegisterPatientForm(UserCreationForm):
    email = forms.EmailField(max_length=100,required = False,help_text='Enter Email Address',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)
    first_name = forms.CharField(max_length=100,required = True,help_text='Enter First Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),)
    middle_name = forms.CharField(max_length=100,required = True,help_text='Enter Last Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),)
    last_name = forms.CharField(max_length=100,required = True,help_text='Enter Last Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)
    username = forms.CharField(max_length=200,required = True,help_text='Enter Username',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    date_of_birth = forms.DateField(required = True, help_text = 'Enter date of birth', input_formats=DATE_INPUT_FORMATS, widget = forms.DateInput(attrs ={'class': 'form-control', 'placeholder': 'dd.mm.yyyy'}),)
    gov_id = forms.CharField(required = True, validators = [only_int],  widget = forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'gov_id','size': 12,}),)
    blood_group = forms.CharField( help_text = 'Enter blood group',label='blood group', widget = forms.Select(choices = BLOOD_GROUPS))
    address = forms.CharField(required = True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),)
    marital_status = forms.CharField(required = True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marital status'}),)
    reg_date = forms.DateField(required = True, help_text = 'Enter date of birth', input_formats=DATE_INPUT_FORMATS, widget = forms.DateInput(attrs ={'class': 'form-control', 'placeholder': 'dd.mm.yyyy'}),)
    class Meta:
        model = User
        fields = ['gov_id', 'date_of_birth','username','first_name','middle_name', 'last_name', 'email','blood_group', 'address','marital_status','reg_date','password1', 'password2']
