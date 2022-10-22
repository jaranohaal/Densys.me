from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# This is our links?

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse('About us')
