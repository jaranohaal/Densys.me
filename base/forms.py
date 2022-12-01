from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Department,Appointment, Doctor

class appointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email', 'phone', 'date','department','doctor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['doctor'].queryset = Doctor.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty doctor queryset
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.department.doctor_set.order_by('name')
