from django.db import models

# Create your models here.

class Product(models.Model):
    cod = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    stock = models.IntegerField()
    CATEGORIAS = (
        (0, ""),
        (1, "Ropa"),
        (2, "Comida"),
        (3, "Electrodoméstico"),
    )
    categoria = models.IntegerField(choices=CATEGORIAS, default=0, null=True, blank=True)
    
    
    class Factura(models.Model):
        fecha = models.DateField(help_text="Fecha de Factura YYYY-MM-DD")
        cliente = models.CharField(max_length=100)
        num_factura = models.IntegerField()
        product = models.ForeignKey('Product', )
    
    #makemigrations tienda => cambios al model 
    
    #migrate
    