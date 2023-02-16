from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from student.forms import *
from student.Email_back_end import Email_back_end
from adduser.models import student, chairman, hallprovost, examcontroller

def home(request):
    return render(request,"home.html")

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
            # first_name=form.cleaned_data["first_name"]
            # last_name=form.cleaned_data["last_name"]
            regi_no=form.cleaned_data["regi_no"]
            name=form.cleaned_data["name"]
            dept_name=form.cleaned_data["dept_name"]
            hall_name=form.cleaned_data["hall_name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_start=form.cleaned_data["session_start"]
            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
            # return HttpResponse("add student")
            try:
                
                user=student( regi_no=regi_no
                             ,dept_name=dept_name,hall_name=hall_name,name=name,email=email, password=password, address=address, session_start=session_start,profile_pic_url=profile_pic_url)
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student"))
            except Exception as e:
                return HttpResponse(e)      
        else:
            form=AddStudentForm(request.POST)
            return render(request, "addStudent.html", {"form": form})
        
def add_chairman(request):
    return render(request,"addchairman.html")

def add_chairman_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        dept_name=request.POST.get("dept_name")
        try:
            user=chairman(dept_name=dept_name, name=name, email=email, password=password)
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
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            hall_name=form.cleaned_data["hall_name"]
            try:
                #user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=3)
                user=hallprovost(hall_name=hall_name, name=name, email=email, password=password)
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
                user=examcontroller(username=username,password=password,email=email,user_type=4)
                user.save()
                messages.success(request,"Successfully Added exam")
                return HttpResponseRedirect(reverse("add_examcontroller"))
            except:
                messages.error(request,"Failed to Add exam")
                return HttpResponseRedirect(reverse("add_examcontroller"))
        else:
            form=AddExamcontrollerForm(request.POST)
            return render(request, "addexamcontroller.html", {"form": form})
