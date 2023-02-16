from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from adduser.models import examcontroller, student
from student.models import registration1, course_model, permission_model
# Create your views here.

def examcontroller1(request):
    return render(request,"examcontroller/examcontroller_login.html")
def examcontroller_login(request):
    if request.method!='POST':
        return HttpResponse("method not allowed")
    else:
        try:
            get_email=request.POST.get("email")
            get_password=request.POST.get("password")
            exists=examcontroller.objects.filter(email=get_email,password=get_password).exists()
            if exists:
                v=examcontroller.objects.filter(email=get_email)
                vs=v.last().dept_name
                data=permission_model.objects.filter(examcontroller_permission=False)
               
                context={'data':data, }
                print(data)
                return render(request,  "examcontroller/examcontroller_home.html", context)
            else:
                msg="You have entered wrong Password or email"
                return render(request,"examcontroller/examcontroller_login.html", {'msg':msg})
            
        except Exception as e:
            return HttpResponse(e)
from django.http import JsonResponse     
def examcontroller_get_info(request):
    if request.method=="POST":
        # print(request.POST)
        regi_no=request.POST.get("regi_no")
        semester_no=request.POST.get("semester_no")
        print(regi_no, semester_no)
        #r_n=regi_no+'/'
        
        data=registration1.objects.filter(regi_no=regi_no, semester_no=semester_no).last()
        data1=course_model.objects.filter(regi_no=regi_no).last()
        data2=student.objects.filter(regi_no=regi_no).last()        
        dic={'name':data2.name,'session':data2.session_start_year,
         'dept_name':data.dept_name, 'hall_name':data.hall_name, 'semester_no':data.semester_no, 
         'bank_receipt':data.bank_receipt,'regi_no':data.regi_no,
            'bank_image':data.bank_receipt_image, 'phn':data.phn_nmbr,
            'course_name':data1.course_name.split(','), 'course_credit':data1.course_credit.split(','),
            'course_code':data1.course_code.split(',')}
        
        return render(request, "examcontroller/examcontroller_info.html", {'all_data':dic})
    else:
        return HttpResponse("method not allowed")

def examcontroller_emnei(request):
    if request.method=="POST":
        val=request.POST.get("ac")
        val1=request.POST.get("wa")
        regi_no=request.POST.get("regi_no")
        semester_no=int(request.POST.get("semester_no"))
        print(val, val1, regi_no, semester_no)
        ex=permission_model.objects.filter(regi_no=regi_no, semester_no=semester_no).first()
        
        print(ex, "hello")
        if val=="ac":
          ex.examcontroller_permission=True
        elif val1=="wa":
            ex.examcontroller_permission=False
        ex.save()
        data=permission_model.objects.filter(examcontroller_permission=0)
        context={'data':data, }
        return render(request,  "examcontroller/examcontroller_home.html", context)
        
    else:
        return HttpResponse("val")
