from django.contrib import admin
from .models import registration1
# Register your models here.

@admin.register(registration1)
class register(admin.ModelAdmin):
    pass

