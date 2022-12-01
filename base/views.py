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

def aboutus(request):
    return HttpResponse('About us')


def appointment(request):
    form = appointmentForm()
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "appointment.html", {"form": form})

def doctors(request):

    data = json.loads(request.body)

    department_id = data['user_id']
    doctors = Doctor.objects.filter(department__id = department_id)
    return JsonResponse(list(doctors.values("department_id","first_name","last_name","photo")), safe = False)


"""
class appointment(TemplateView):
    template_name = 'appointment.html'

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneNum = request.POST.get('number')
        date = request.POST.get('date')
        department = request.POST.get('department')
        appointment = Appointment.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            phone = phoneNum,
            date = date,
            department = department
        )
        appointment.save()

        messages.success(request, 'appointment request sent for user ' + fname +' '+ lname)
        return HttpResponseRedirect(request.path)
"""
def loginPage(request):
    context = {}
    return render(request,'login.html', context)
