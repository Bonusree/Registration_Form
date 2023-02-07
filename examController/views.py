from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View

# Create your views here.

def examcontroller(request):
    return render(request, 'examcontroller/examcontrol_login.html' )
