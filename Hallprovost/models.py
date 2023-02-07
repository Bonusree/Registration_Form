from django.db import models

# Create your models here.
class hlog(models.Model):
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)
    