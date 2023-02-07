from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import ExampleForm,Image1,Image2
from .models import registration1,Image
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from .models import PdfFile
from .forms import PdfForm
import pdfkit
import os
# Create your views here.
email=''
password=''
def student(request):
    return render(request,"student/student_login.html")
    
def registration1(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            return redirect('some_view_name')
    else:
        form = ExampleForm()

    context = {'form': form}
    return render(request, 'student/student_registration1.html', context)

def image(request):
     if request.method == 'POST':
        Image_form = Image1(request.POST, request.FILES)
        text_form = Image2(request.POST, request.FILES)
        if Image_form.is_valid() and text_form.is_valid():
            
            # create a PDF using the uploaded image
            Image_form = request.FILES['Image']
            text_form = request.FILES['Image']
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawImage(image, 10, 10)
            p.save()
            buffer.seek(0)
            # return FileResponse(buffer, as_attachment=True, filename='image.pdf')
            return HttpResponseRedirect()
     else:
        Image_form=Image1()
        text_form=Image2()
     return render(request, 'student/image_uploader.html', {'Image_form':Image_form, 'text_form':text_form})
 
def generate_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.save()
            template = get_template('student/pdf_template.html')
            context = {'pdf_file': pdf_file}
            html = template.render(context)
            pdf = pdfkit.from_string(html, False)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + pdf_file.pdf_file + '.pdf"'
            return response
    else:
        form = PdfForm()
    return render(request, 'student/generate_pdf.html', {'form': form})