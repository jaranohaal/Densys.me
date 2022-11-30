from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Appointment

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse('About us')

class appointment(TemplateView):
    template_name = 'appointment.html'

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneNum = request.POST.get('number')
        date = request.POST.get('date')

        appointment = Appointment.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            phone = phoneNum,
            date = date
        )
        appointment.save()

        messages.success(request, 'appointment request sent for user ' + fname +' '+ lname)
        return HttpResponseRedirect(request.path)

def loginPage(request):
    context = {}
    return render(request,'login.html', context)
