#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
DATE_INPUT_FORMATS = ['%d.%m.%Y']
