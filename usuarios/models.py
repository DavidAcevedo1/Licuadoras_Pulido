from django.db import models
from django.utils.translation import gettext_lazy as _

class Producto(models.Model):
    imagen = models.ImageField(upload_to="carrito", null=True, blank=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descuento = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
 
