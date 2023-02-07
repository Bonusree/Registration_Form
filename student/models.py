from django.db import models

# Create your models here.
class slog(models.Model):
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)
    
class registration1(models.Model):
    name=models.CharField(max_length=250, default=True)
    dept_name=models.CharField(max_length=250, default=True)
    regi_no=models.CharField(max_length=250, primary_key=True)
    session=models.CharField(max_length=250, default=True)
    zilla=models.CharField(max_length=250,default=True)
    post_office=models.CharField(max_length=250, default=True)
    village=models.CharField(max_length=250, null=True)
    email=models.EmailField(max_length=250, unique=True, default=True)
    # birth_date=models.DateField(auto_created=True)
    phn_nmbr=models.CharField(max_length=250, null=True)
    


class Image(models.Model):
    image_1= models.ImageField(upload_to="my_image")
    image_2= models.ImageField(upload_to="my_image")
    date= models.DateTimeField(auto_now_add=True)
    


class coursecode(models.Model):
    course_id=models.AutoField(primary_key=True, null=False, default=1)
    course_name=models.CharField(max_length=250, null=False)
    course_code=models.CharField(max_length=250, null=False)
    course_credit=models.CharField(max_length=250, null=False)
    objects=models.Manager()
    
class PdfFile(models.Model):
    file_name = models.CharField(max_length=100)
    email = models.EmailField()
    pdf_file = models.FileField(upload_to='pdf/')