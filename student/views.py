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
        st=regi_no+'\n'+regi_no
        buffer= io.BytesIO()
        p= canvas.Canvas(buffer)
        
        p.drawString(200, 700, "registration no: "+st)
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer,  content_type='application/pdf')
    # # Get the user input
    
    #     text=str(request.GET.get('text'))
    #     chobi=str(request.GET.get('chobi'))
    #     # user=registration1(text=text, chobi=chobi)
    #     # user.save()
    #     # text=str(user)
        
    # # Create a file-like buffer to receive PDF data.
    #     buffer = io.BytesIO()

    # # Create the PDF object, using the buffer as its "file."
    #     p = canvas.Canvas(buffer)

    # # Draw things on the PDF. Here's where the PDF generation happens.
    #     p.drawS(200, 700, "User Input: " + text
    #                  +chobi)
       
    # # Close the PDF object cleanly, and we're done.
    #     p.showPage()
    #     p.save()

    # # FileResponse sets the Content-Disposition header so that browsers
    # # present the option to save the file.
    #     buffer.seek(0)
    #     file = InMemoryUploadedFile(buffer, None, 'user_input.pdf', 'application/pdf', buffer.getbuffer().nbytes, None)

    # # Store the PDF file in the database
    #     pdf =store_pdf( pdf_file=file )
    #     pdf.save()

       # return HttpResponse(regi_no)
