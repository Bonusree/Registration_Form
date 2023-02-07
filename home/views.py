import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from home.forms import *
from home.Email_back_end import Email_back_end
from home.models import *

def home(request):
    return render(request,"home.html")

# def ShowLoginPage(request):
#     return render(request,"login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        #return HttpResponse("<h2>Method is Allowed</h2>")
        user=Email_back_end.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponse('stuent')
            elif user.user_type=="2":
                return HttpResponseRedirect('chairman')
            elif user.user_type=="3":
                return HttpResponseRedirect('provost')
            else:
                return HttpResponseRedirect('exam')
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def add_student(request):
    form=AddStudentForm()
    return render(request,"addStudent.html",{"form":form})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        #return HttpResponse("<h2>student is Allowed</h2>")
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            id=form.cleaned_data["id"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_start=form.cleaned_data["session_start"]
            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,name=name,user_type=1)
                user.student.address=address
                user.student.id=id
                user.student.session_start_year=session_start
                user.student.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "addStudent.html", {"form": form})
        
def add_chairman(request):
    return render(request,"addchairman.html")

def add_chairman_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        dept_name=request.POST.get("dept_name")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
            user.chairmans.dept_name=dept_name
            user.save()
            messages.success(request,"Successfully Added chairman")
            return HttpResponseRedirect(reverse("add_chairman"))
        except:
            messages.error(request,"Failed to Add chairman")
            return HttpResponseRedirect(reverse("add_chairman"))
        
def add_hallprovost(request):
    form=AddHallprovostForm()
    return render(request,"addhallprovost.html",{"form":form})

def add_hallprovost_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddHallprovostForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            hall_name=form.cleaned_data["hall_name"]
            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=3)
                user.hallprovost.hall_name=hall_name
                user.save()
                messages.success(request,"Successfully Added hallprovost")
                return HttpResponseRedirect(reverse("add_hallprovost"))
            except:
                messages.error(request,"Failed to Add hallprovost")
                return HttpResponseRedirect(reverse("add_hallprovost"))
        else:
            form=AddHallprovostForm(request.POST)
            return render(request, "addhallprovost.html", {"form": form})

def add_examcontroller(request):
    form=AddExamcontrollerForm()
    return render(request,"addexamcontroller.html",{"form":form})

def add_examcontroller_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddExamcontrollerForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=4)
                user.save()
                messages.success(request,"Successfully Added exam")
                return HttpResponseRedirect(reverse("add_examcontroller"))
            except:
                messages.error(request,"Failed to Add exam")
                return HttpResponseRedirect(reverse("add_examcontroller"))
        else:
            form=AddExamcontrollerForm(request.POST)
            return render(request, "addexamcontroller.html", {"form": form})

