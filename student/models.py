from django.db import models

# Create your models here.
class permission_model(models.Model):
    dept_name=models.CharField(max_length=250, default="cse")
    hall_name=models.CharField(max_length=250, default="hall")
    semester_no=models.IntegerField( default=1)
    regi_no=models.CharField(max_length=250,  default="0")
    chairman_permission=models.BooleanField(default=False)
    examcontroller_permission=models.BooleanField( default=False)
    hallprovost_permission=models.BooleanField( default=False)
    
class registration1(models.Model):
    dept_name=models.CharField(max_length=250, default="cse")
    hall_name=models.CharField(max_length=250, default="hall")
    regi_no=models.CharField(max_length=250, default="0")
    phn_nmbr=models.CharField(default="01", max_length=30)
    semester_no=models.IntegerField( default=1)
    bank_receipt=models.CharField(default="11",max_length=30)
    bank_receipt_image=models.FileField()
   
    
class course_model(models.Model):
    semester_no=models.IntegerField( default=1)
    regi_no=models.CharField(max_length=250,  default="0")
    course_name=models.CharField(max_length=250, default="true")
    course_code=models.CharField(max_length=250, default="true")
    course_credit=models.CharField(max_length=250, default="true")
    

