from django.contrib import admin
from .models import travelmodel

class travel1(admin.ModelAdmin):
    list_display = ("main_img_src","categori","main_heading","description","img_src_two","description_two","img_src_three","description_three","img_src_four","img_src_five","description_four","img_src_six","new_slug")

    
admin.site.register(travelmodel,travel1)
# Register your models here.
