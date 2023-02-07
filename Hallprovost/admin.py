from django.contrib import admin
from .models import hlog
# Register your models here.
@admin.register(hlog)
class log_admin(admin.ModelAdmin):
    list_display=['email', 'password']