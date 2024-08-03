from django.contrib import admin
from .models import lifestylemodel

class life(admin.ModelAdmin):
    list_display = ("main_img_src","categori","main_heading","description","img_src_two","description_two","img_src_three","description_three","img_src_four","img_src_five","description_four","img_src_six","new_slug")
    
admin.site.register(lifestylemodel,life)
    
# Register your models here.
