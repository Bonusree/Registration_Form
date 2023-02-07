from django.contrib import admin
from .models import clog
# Register your models here.
@admin.register(clog)
class log_admin(admin.ModelAdmin):
    list_display=['email', 'password']