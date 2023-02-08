from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import *
from django.core.files.storage import FileSystemStorage
from .models import *
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
import pdfkit
import os
# Create your views here.
email=''
password=''
def student(request):
    return render(request,"student/student_login.html")
def regi_show(request):
    form =registraion()
    return render(request, "student/student_registration1.html",{"form":form})   

    
def regi_complete(request):      
        if request.method != 'POST':
            return HttpResponse("method not allowed")
        else:
            try:
                form = registraion(request.POST,request.FILES)
                if form.is_valid():
                    dept_name=form.cleaned_data["dept_name"]
                    regi_no=form.cleaned_data["regi_no"]
                    phn_nmbr=form.cleaned_data["phn_nmbr"]
                    semester_no=form.cleaned_data["semester_no"]
                    bank_receipt=form.cleaned_data["bank_receipt"]
                    courses=form.cleaned_data["courses"]
                    bank_receipt_image=request.FILES['bank_receipt_image']
                    fs=FileSystemStorage()
                    filename=fs.save(bank_receipt_image.name,bank_receipt_image)
                    bank_receipt_image_url=fs.url(filename)
                    try:
                        user=registration1.objects.create(dept_name=dept_name, regi_no=regi_no, phn_nmbr=phn_nmbr,
                                        semester_no=semester_no , bank_receipt=bank_receipt,
                                       courses=courses, bank_receipt_image=bank_receipt_image_url)
                        user.save()
                        return HttpResponse("some_view_name")
                    except Exception as e:
                        return HttpResponse(e)
                else:
                    return HttpResponse("method not posted")
            except Exception as e:
                return HttpResponse(e)
        # else:
        #    return HttpResponse("method not posted")
    
            


 
# def generate_pdf(request):
#     if request.method == 'POST':
#         form = PdfForm(request.POST, request.FILES)
#         if form.is_valid():
#             pdf_file = form.save()
#             template = get_template('student/pdf_template.html')
#             context = {'pdf_file': pdf_file}
#             html = template.render(context)
#             pdf = pdfkit.from_string(html, False)
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="' + pdf_file.pdf_file + '.pdf"'
#             return response
#     else:
#         form = PdfForm()
#     return render(request, 'student/generate_pdf.html', {'form': form})