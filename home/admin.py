from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserModel(UserAdmin):
    pass

class userstudent(admin.ModelAdmin):
    pass
class userchairman(admin.ModelAdmin):
    pass
class userhallprovost(admin.ModelAdmin):
    pass
class userexamcontroller(admin.ModelAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(student,userstudent)
admin.site.register(chairman,userchairman)
admin.site.register(hallprovost,userhallprovost)
admin.site.register(examcontroller,userexamcontroller)