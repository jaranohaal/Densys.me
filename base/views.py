from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, RegisterForm
from django.contrib import messages
# Create your views here.
# This is our links?

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse('About us')

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form' : form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})
def registerPage(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form .is_valid():
             form.save()
    messages.success(request, 'Account created successfully')
    context = {'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    context = {}
    return render(request,'login.html', context)
