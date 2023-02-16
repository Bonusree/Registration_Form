from django import forms

from django.core.exceptions import ValidationError
    
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
class registraion(forms.Form):
    dept_name=forms.CharField(label="dept_name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    regi_no=forms.CharField(label="regi_no",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    phn_nmbr=forms.CharField(label="phn_nmbr",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    semester_no=forms.IntegerField(label="Semester no",widget=forms.TextInput(attrs={"class":"form-control"}) )
    bank_receipt=forms.IntegerField(label="bank_receipt",widget=forms.TextInput(attrs={"class":"form-control"}) )
    courses=forms.IntegerField(label="Number of courses",widget=forms.TextInput(attrs={"class":"form-control"}) )
    bank_receipt_image=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
    


# class Image2(forms.Form):
#     other=forms.ImageField(label='Upload Your all bankdraft as pdf')
    



# class PdfForm(forms.ModelForm):
#     class Meta:
#         model = PdfFile
#         fields = ['file_name', 'email', 'pdf_file']
