from django.contrib import admin

# Register your models here.

#python3 manage.py createsuperuser

from .models import *
admin.site.register(Product)