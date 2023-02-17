from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from django.core.files.storage import FileSystemStorage
from student.models import registration1, course_model, permission_model
from adduser.models import student
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from django.db.models import Q
from django.db import connections
from django.template import loader
import pdfkit
import os
from django.conf import settings 
from ..Registration_Form import settings

# base_dir_name = os.path.basename(os.getcwd())

# Create your views here 
exists=''
password=''
def student1(request):
    return render(request,"student/student_login.html")
def student_login(request):
    if request.method!='POST':
        return HttpResponse("method not allowed")
    else:
        try:
            get_email=request.POST.get("email")
            get_password=request.POST.get("password")
            v=student.objects.all().values()
            exists=student.objects.filter(email=get_email,password=get_password).exists()
            val=student.objects.filter(email=get_email,password=get_password)
            if exists:
                return render(request,  "student/student_home.html", {'regi_no':val.last().regi_no})
            else:
                return HttpResponse(v)
            
        except Exception as e:
            return HttpResponse(e)
        
def student_home(request):
    return render(request,'student/student_registration1.html')           

def regi_complete(request):      
        if request.method != 'POST':
            return HttpResponse("method not allowed")
        else:
            try:
                dept_name=request.POST.get("dept_name")
                regi_no=request.POST.get("regi_no")
                phn_nmbr=request.POST.get("phn_nmbr")
                bank_receipt=request.POST.get("bank_receipt")
                semester_no=(request.POST.get("semester_no"))
                hall_name=(request.POST.get("hall_name"))
                bank_receipt_image=request.FILES['bank_receipt_image']
                fs=FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media')) 
                filename=fs.save(bank_receipt_image.name,bank_receipt_image)
                bank_receipt_image_url=fs.url(filename) 
                print('agdagiyat',fs.url(filename))
                
                s_e=student.objects.filter(regi_no=regi_no, dept_name=dept_name, hall_name=hall_name).exists()
                if s_e==False:
                    msg="You have entered any Wrong Information"
                    return render(request, 'student/student_registration1.html', {'msg':msg})
                exist=registration1.objects.filter(regi_no=regi_no, semester_no=semester_no).exists()
                if exist==True:
                    msg="you have already registered"
                    return render(request, 'student/student_registration1.html', {'msg':msg})
                try:
                    regi_form=registration1(dept_name=dept_name, regi_no=regi_no,hall_name=hall_name,
                                            phn_nmbr=phn_nmbr, bank_receipt=bank_receipt,
                                            semester_no=semester_no, 
                                            bank_receipt_image=bank_receipt_image_url)
                    regi_form.save()
                    per=permission_model(regi_no=regi_no, semester_no=semester_no, 
                                         hall_name=hall_name, dept_name=dept_name,
                        chairman_permission=False , examcontroller_permission=False,
                        hallprovost_permission=False)
                    per.save()
                except Exception as e:
                    return HttpResponse(e)
            except Exception as e:
                return HttpResponse(e)
        
            dic={'semester_no':semester_no,  'regi_no':regi_no}
            return render(request, 'student/courses.html', {'semester_no':semester_no,  'regi_no':regi_no})
       
def get_courses(request):
    if request.method!='POST':
        return render(request, 'student/courses.html')
    else:
        courses=int(request.POST.get("output"))
        semester_no=int(request.POST.get("semester_no")[0:-1])
        regi_no=request.POST.get("regi_no")[0:-1]
        c_n=''
        c_c=''
        c_t=''
        for i in range(0,courses):
            print("\n\n\ni+1",i+1)
            course_name=request.POST.get(f"course_name{i+1}")
            course_code=request.POST.get(f"course_code{i+1}")
            course_credit=request.POST.get(f"course_credit{i+1}")
            c_n+=course_name+','
            c_c+=course_code+','
            c_t+=course_credit+','
           
        c=course_model(semester_no=semester_no, regi_no=regi_no,
                           course_name=c_n, course_code=c_c,
                           course_credit=c_t)
        c.save()
        
        msg="your registration has completed"
        return render(request, 'student/student_home.html', {'msg':msg})
            
def get_admit(request):
    if request.method == 'POST':
        regi_no=request.POST.get("regi_no")
        ex=permission_model.objects.filter(regi_no=regi_no, 
                                           chairman_permission=True, 
                                           examcontroller_permission=True,
                                           hallprovost_permission=True).exists()
        if ex:
            val=registration1.objects.filter(regi_no=regi_no)
            context={'data':val}
            return render(request,  "student/get_admit.html", context)
        else:
            return HttpResponse()
            
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import FileResponse
from reportlab.pdfgen import canvas
import pdfkit 
# from django.template.loader import get_template
from django.http import HttpResponse
# from django.views.generic import View
# from django_wkhtmltopdf.views import PDFTemplateView

def generate_pdf(request):
    if request.method == 'POST':
        regi_no=request.POST.get("regi_no")
        semester_no=request.POST.get("semester_no")
        data=registration1.objects.filter(regi_no=regi_no, semester_no=semester_no).last()
        data2=student.objects.filter(regi_no=regi_no).last()        
        dic={'name':data2.name,'session':data2.session_start_year,
         'dept_name':data.dept_name, 'hall_name':data.hall_name, 'semester_no':data.semester_no, 
         'regi_no':data.regi_no}
        print("hello")
        createAdmit(dic)
        
        pdf = os.path.join(settings.BASE_DIR,'try.pdf')
        with open(pdf, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf}"'
            return response
       
        # buffer= io.BytesIO()
        # p= canvas.Canvas(buffer)
    
        # p.drawString(200, 700, "registration no: "+st+v)
        # p.showPage()
        # p.save()
        # buffer.seek(0)
        # return FileResponse(buffer,  content_type='application/pdf')
    return HttpResponse("kisu nai")
    
options = {
    'page-size': 'A4',
    'margin-top': '5mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'orientation': 'Landscape',
    'encoding': "UTF-8"
}
def createAdmit(dic):
    html = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
        .container{{
            width: 936px;
            height: 445px;
            border: 1px solid black;
            margin: 0 auto;
            padding-top: 5px;
            padding-bottom: 10px;
        }}
        .container ul{{
            list-style-type: none;
        }}
        .header{{
            background-color: #eeeedd;
            padding: 10px 0px;
            display: flex;
        }}
        .header table{{
            width: 50%;
            margin: 0 auto;
        }}
        .header table td{{
            padding: 0px;
        }}
        .information table{{
            padding: 10px 0px;
            font-size: 20px;
            display: flex;
            width: 95%;
            /* border: 1px solid; */
            margin: auto;
        }}
        .information table tr,td{{
            padding-top: 10px;
        }}
        .info-box{{
            margin: 0px 5px;
            border-bottom: 1px dotted;
            width: 450px;
        }}
        img{{
            height: 80px;
            width: 80px;
        }}
        .sign{{
            margin-top: 30px;
        }}
        .sign table{{
            width: 90%;
            margin: 0px auto;
        }}
        .sign table td{{
            padding: 0px;
        }}
        .footer{{
            background-color: #eeeedd;
            padding: 10px 0px;
            text-align: center;
        }}
    </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <table>
                    <tr>
                        <td rowspan="3"><img src="https://upload.wikimedia.org/wikipedia/commons/archive/8/8e/20130209134529%21COU_LOGO.jpg"/></td>
                        <td style="font-size: 40px; text-align: center; font-weight: bold;">Comilla University</td>
                    </tr>
                    <tr>
                        <td style="font-size: 20px; text-align: center; ">Cumilla-3506</td>
                    </tr>
                    <tr>
                        <td style="background-color: black; color:white; font-size: 35px; text-align: center; font-weight: bold;">ADMIT CARD</td>
                    </tr>
                    <tr>
                        <td colspan="3" style="font-size: 20px; font-weight: bold; text-align: right;">
                            {dic['semester_no']} Semester Final Examination 2022
                        </td>
                    </tr>
                </table>
            </div>
            
            <div class="information">
                <table>
                    <tr>
                        <td>Name of the Students: </td>
                        <td colspan="3"><div class="info-box">{dic['name']}</div></td>
                    </tr>
                    <tr>
                        <td>Hall Name: </td>
                        <td colspan="3"><div class="info-box">{dic['hall_name']}</div></td>
                    </tr>
                    <tr>
                        <td>Department: </td>
                        <td colspan="2"><div class="info-box" style="width: 300px;">{dic['dept_name']}</div></td>
                        <td>Registration No: </td>
                        <td><div class="info-box" style="width: 150px;">{dic['regi_no']}</div></td>
                    </tr>
                    <tr>
                        <td>Session: </td>
                        <td ><div class="info-box" style="width: 150px;">{dic['session']}</div></td>
                        <td>Examination Roll No: </td>
                        <td colspan="2"><div class="info-box" style="width: 200px;">{dic['regi_no']}</div></td>
                    </tr>
                </table>
            </div>
            <div class="sign">
                <table>
                    <tr>
                        <td>----------------------------------</td>
                        <td style="text-align: right;">----------------------------------</td>
                    </tr>
                    <tr>
                        <td>Signature of Student</td>
                        <td style="text-align: right;">Controller of Examination's</td>
                    </tr>
                </table>
            </div>
            <div class="footer">
                it is footer line
            </div>  
        </div>
    </body>
</html>
    """
    with open("generated.html", "w") as file:
            file.write(html)
    config = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')        
    pdfkit.from_file('generated.html', 'try.pdf',configuration=config,options=options)
    # os.startfile('try.pdf')

# createAdmit()