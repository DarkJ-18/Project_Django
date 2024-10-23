from django.db import models

# Create your models here.
#makemigrations tienda => cambios al model 
#migrate
#python3 manage.py createsuperuser => admin

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
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - ({self.stock} unidades)"
    
class Factura(models.Model):
    fecha = models.DateField(help_text="Fecha de Factura YYYY-MM-DD")
    cliente = models.CharField(max_length=100)
    num_factura = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.num_factura} - {self.cliente}"
    

