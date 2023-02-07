from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import cman
# Create your views here.

def chairman(request):
    return render(request, 'chairman/chairman_login.html' )
