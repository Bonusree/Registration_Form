from django.contrib import admin
from .models import elog
# Register your models here.
@admin.register(elog)
class log_admin(admin.ModelAdmin):
    list_display=['email', 'password']