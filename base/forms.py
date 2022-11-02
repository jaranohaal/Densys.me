#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
DATE_INPUT_FORMATS = ['%d.%m.%Y']
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,required = True,help_text='Enter Email Address',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)
    first_name = forms.CharField(max_length=100,required = True,help_text='Enter First Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),)
    last_name = forms.CharField(max_length=100,required = True,help_text='Enter Last Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)
    username = forms.CharField(max_length=200,required = True,help_text='Enter Username',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    check = forms.BooleanField(required = True)
    date_of_birth = forms.DateField(required = True, help_text = 'Enter date of birth', input_formats=DATE_INPUT_FORMATS, widget = forms.DateInput(attrs ={'class': 'form-control', 'placeholder': 'dd.mm.yyyy'}),)
    gov_id = forms.CharField(required = True, validators = [only_int],  widget = forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'gov_id','size': 12,}),)

    class Meta:
        model = User
        fields = ['gov_id', 'date_of_birth','username','first_name', 'last_name', 'email', 'password1', 'password2','check']
