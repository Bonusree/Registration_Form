from django.contrib import admin
from .models import registration1, course_model, permission_model
# Register your models here.

@admin.register(registration1)
class regi(admin.ModelAdmin):
    pass

@admin.register(course_model)
class c_m(admin.ModelAdmin):
    pass

@admin.register(permission_model)
class register(admin.ModelAdmin):
    pass

