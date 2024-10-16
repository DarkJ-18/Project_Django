from django.contrib import admin

# Register your models here.

#python3 manage.py createsuperuser

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'nombre', 'precio','categoria','stock']
    search_fields = ['nombre', 'cod', 'categoria', 'stock']
    list_filter = ['cod','categoria']
    list_editable = ['nombre', 'categoria','stock']
    
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'num_factura','product']
    search_fields = ['fecha', 'cliente', 'num_factura']
    list_filter = ['fecha','cliente']
    list_editable = ['fecha', 'product','num_factura']

