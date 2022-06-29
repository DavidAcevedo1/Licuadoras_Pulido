from django.db import models
from django.utils.translation import gettext_lazy as _
from administrador.models import Elemento
from usuarios.models import  Usuario

class Factura(models.Model):
    fecha=models.DateField(auto_now = True, verbose_name="Fecha de factura", help_text=u"MM/DD/AAAA")
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Trabajador='Trabajador', _('Trabajador')
    rol= models.CharField(max_length=13,null=True, choices=Rol.choices, verbose_name="rol")      
    usuario=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,verbose_name="Nombre")
    class Tipofactura(models.TextChoices):
        Compra='Compra', _('Compra')
        Venta='Venta', _('Venta')
    tipofactura= models.CharField(max_length=10, choices=Tipofactura.choices, verbose_name="Tipo de factura")
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    class Meta:
        db_table="facturas_factura"
        
class Detalle(models.Model):
    factura=models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True,verbose_name="Factura")
    elemento=models.ForeignKey(Elemento, on_delete=models.SET_NULL, null=True,verbose_name="Elemento")
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADa='Anulada', _('Anulada')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    cantidad=models.IntegerField()
    def __str__(self)-> str:
        return '%s' % (self.id)
    

        