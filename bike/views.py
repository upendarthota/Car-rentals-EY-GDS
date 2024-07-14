from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Python Functions

def home(request):
    
    return HttpResponse('This is Bike Module...!')

 