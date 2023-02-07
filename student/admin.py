from django.contrib import admin
from .models import registration1,slog,Image
# Register your models here.
@admin.register(slog)
class log_admin(admin.ModelAdmin):
    list_display=['email', 'password']
    
@admin.register(registration1)
class register(admin.ModelAdmin):
    list_display=['dept_name','name','session',
                  'regi_no','zilla','post_office','village', 'email', 'phn_nmbr',]

class image(admin.ModelAdmin):
    list_display=('id', 'image_1', 'image_2', 'date',)
admin.site.register(Image, image)