from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# This is our links?

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse('About us')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form .is_valid():
             form.save()

    context = {'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    context = {}
    return render(request,'login.html', context)
