from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Appointment, Doctor, Department
from django.http import JsonResponse
import json
from .forms import appointmentForm

def home(request):
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')

def aboutus(request):
    return HttpResponse('About us')


def appointment(request):
    form = appointmentForm()
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success/')
    return render(request, "appointment.html", {"form": form})

def doctors(request):

    data = json.loads(request.body)

    department_id = data['user_id']
    doctors = Doctor.objects.filter(department__id = department_id)
    return JsonResponse(list(doctors.values("id_doctor","first_name","last_name")), safe = False)



def loginPage(request):
    context = {}
    return render(request,'login.html', context)
