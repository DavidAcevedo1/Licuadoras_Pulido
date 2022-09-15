from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import  Usuario, Rol
from administrador.models import Elemento, Servicio

class Factura(models.Model):
    fecha=models.DateField(auto_now = True, verbose_name="Fecha de factura", help_text=u"MM/DD/AAAA")
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True,verbose_name="Rol")
    usuario=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,verbose_name="Nombre")
    servicio=models.ForeignKey(Servicio, on_delete=models.SET_NULL,blank=True, null=True,verbose_name="Servicio")
    class Tipofactura(models.TextChoices):
        Compra='Compra', _('Compra')
        Venta='Venta', _('Venta')
    tipofactura= models.CharField(max_length=10, choices=Tipofactura.choices, verbose_name="Tipo de factura")
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    class Decision(models.TextChoices):
        ACTIVO= 'Activo', _('Activo')
        INACTIVO= 'Inactivo', _('Inactivo')
    decision= models.CharField(max_length=10, choices=Decision.choices, verbose_name="Estado", default=Decision.ACTIVO)
    class Meta:
        db_table="facturas_factura"
        
class Detalle(models.Model):
    factura=models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True,verbose_name="Factura")
    elemento=models.ForeignKey(Elemento, on_delete=models.SET_NULL, null=True,verbose_name="elemento")
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    cantidad=models.IntegerField()
    total= models.FloatField(default=0 )
    def __str__(self)-> str:
        return '%s' % (self.id)
    
    


#Servicios David 
class DetalleServicio(models.Model):
    factura=models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True,verbose_name="Factura")
    servicio=models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True,verbose_name="servicio")
    elemento=models.ForeignKey(Elemento, on_delete=models.SET_NULL, null=True,verbose_name="elemento")
    class Estado(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ABIERTA)
    cantidad=models.IntegerField()
    costo=models.IntegerField(verbose_name="Costo")
    def __str__(self)-> str:
        return '%s' % (self.id)    
# Final servicios david