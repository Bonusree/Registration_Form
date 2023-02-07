from django import forms
from .models import PdfFile
class sman(forms.Form):
    Email=forms.EmailField(label='email', max_length=250)
    Password=forms.CharField(label='Password', widget=forms.PasswordInput, max_length=250)
    
class ExampleForm(forms.Form):
    name=forms.CharField(label='Student Name',max_length=250 )
    dept_name=forms.CharField(label='Department Name',max_length=250)
    regi_no=forms.CharField(label='Registration no',max_length=250 )
    session=forms.CharField(label='Session',max_length=250)
    zilla=forms.CharField(label='DIstrict',max_length=250)
    post_office=forms.CharField(label='Post Office',max_length=250)
    village=forms.CharField(label='village',max_length=250)
    email=forms.EmailField(label='Student E-mail')
    phn_nmbr=forms.CharField(max_length=15,label='Phone number')
# class date(forms.Form):
#     birth_date=forms.DateField(input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         }), label='Birth Date')
class Image1(forms.Form):
    profile_photo=forms.ImageField(label='Upload Your Photo')

class Image2(forms.Form):
    other=forms.ImageField(label='Upload Your all bankdraft as pdf')
    



class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfFile
        fields = ['file_name', 'email', 'pdf_file']
