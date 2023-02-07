from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View

# Create your views here.

def hallprovost(request):
    return render(request, 'hallprovost/hallprovost_login.html' )
