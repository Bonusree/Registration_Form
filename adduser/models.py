from django.db import models
class student(models.Model):
    id=models.AutoField(primary_key=True)
    regi_no=models.TextField(default=True)
    address=models.TextField(default=True)
    profile_pic=models.FileField(default=True)
    session_start_year=models.DateField(blank=True, null=True)
    dept_name=models.TextField(default=True)
    hall_name=models.TextField(default=True)
    name=models.CharField(default=True, max_length=150)
    password=models.CharField(default=True, max_length=150)
    email=models.EmailField(default=True)
    
  
class chairman(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(default=True, max_length=150)
    password=models.CharField(default=True, max_length=150)
    email=models.EmailField(default=True)
    dept_name=models.CharField(max_length=150,  default=True)
   

class hallprovost(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(default=True,max_length=150)
    password=models.CharField(default=True,max_length=150)
    email=models.EmailField(default=True)
    hall_name=models.TextField(default=True)
    

class examcontroller(models.Model):
    id=models.AutoField(primary_key=True)
    dept_name=models.TextField(default=True)
    name=models.CharField(default=True,max_length=150)
    password=models.CharField(default=True,max_length=150)
    email=models.EmailField(default=True)
    
