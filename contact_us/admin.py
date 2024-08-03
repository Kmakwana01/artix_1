from django.contrib import admin
from .models import contactemodel

class contact(admin.ModelAdmin):
    list_display = ("name","email","fav_categori","message")
    
admin.site.register(contactemodel,contact)
# Register your models here.