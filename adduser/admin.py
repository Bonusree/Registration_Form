from django.contrib import admin

from .models import *

class userstudent(admin.ModelAdmin):
    pass
class userchairman(admin.ModelAdmin):
    pass
class userhallprovost(admin.ModelAdmin):
    pass
class userexamcontroller(admin.ModelAdmin):
    pass

#admin.site.register(CustomUser,UserModel)
admin.site.register(student,userstudent)
admin.site.register(chairman,userchairman)
admin.site.register(hallprovost,userhallprovost)
admin.site.register(examcontroller,userexamcontroller)