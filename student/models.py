from django.db import models

# Create your models here.

class registration1(models.Model):
    dept_name=models.CharField(max_length=250, default=True)
    regi_no=models.CharField(max_length=250, primary_key=True)
    phn_nmbr=models.CharField(max_length=250, unique=True, default=True)
    semester_no=models.IntegerField(blank=False, default=True)
    bank_receipt=models.IntegerField(default=True, unique=True)
    courses=models.IntegerField(default=True)
    bank_receipt_image=models.FileField(default=True)



class coursecode(models.Model):
    course_id=models.AutoField(primary_key=True, null=False, default=1)
    course_name=models.CharField(max_length=250, null=False)
    course_code=models.CharField(max_length=250, null=False)
    course_credit=models.CharField(max_length=250, null=False)
    objects=models.Manager()
    
