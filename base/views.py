from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterPatientForm
from django.contrib import messages
# Create your views here.
# This is our links?

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse('About us')

def registerPatient(request):
    if request.method == 'GET':
        form = RegisterPatientForm()
        context = {'form' : form}
        return render(request, 'registerpatient.html', context)
    if request.method == 'POST':
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home_page')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'registerpatient.html', context)

    return render(request, 'registerpatient.html', {})

def loginPage(request):
    context = {}
    return render(request,'login.html', context)
