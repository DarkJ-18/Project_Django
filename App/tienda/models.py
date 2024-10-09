from django.db import models

# Create your models here.

class Product(models.Model):
    cod = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    
    #makemigrations tienda => cambios al model 
    
    #migrate
    