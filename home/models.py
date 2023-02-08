from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    user_type_data=((1,"student"),(2,"chairman"),(3,"hallprovost"),(4,"examcontroller"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    id=models.TextField(primary_key=True)
    address=models.TextField(default=True)
    profile_pic=models.FileField(default=True)
    session_start_year=models.DateField(blank=True, null=True)
    dept_name=models.TextField(default=True)
    objects=models.Manager()
  
class chairman(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    dept_name=models.CharField(max_length=150,  default=True)
    objects=models.Manager()

class hallprovost(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    hall_name=models.TextField(default=True)
    objects=models.Manager()

class examcontroller(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects=models.Manager()
    
@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            student.objects.create(admin=instance,id="", session_start_year="2020-01-01",address="", dept_name="")
        if instance.user_type==1:
            chairman.objects.create(admin=instance, dept_name="" )
        if instance.user_type==1:
            hallprovost.objects.create(admin=instance, hall_name="")
        if instance.user_type==1:
            examcontroller.objects.create(admin=instance)
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.student.save()
    if instance.user_type==2:
        instance.chairman.save()
    if instance.user_type==3:
        instance.hallprovost.save()
    if instance.user_type==4:
        instance.examcontroller.save()