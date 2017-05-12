from django.contrib import admin
from .models import *
# Register your models here.

class employee_data_Admin(admin.ModelAdmin):
    list_display=["name","email","manager"]
admin.site.register(employee_data,employee_data_Admin)

# class hierarchy_data_Admin(admin.ModelAdmin):
#     list_display=["junior","senior"]
# admin.site.register(hierarchy_data,hierarchy_data_Admin)