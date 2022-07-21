# from xml.dom.minidom import Element
from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.sql']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Archivo no válido')

class Copiaseguridad(models.Model):
    nombre = models.CharField(max_length = 200,default="Copia de Seguridad", blank=True)
    archivo = models.FileField(upload_to = "copiaseguridad",validators=[validate_file_extension])
    fecha = models.DateTimeField(auto_now = True)

class Marca(models.Model):
    nombre= models.CharField(max_length=10)
    class Estado(models.TextChoices):
        ACTIVO='Activo',_('Activo')
        INACTIVO='Inactivo',_('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s'%(self.nombre)
    def clean(self):
        self.nombre= self.nombre.title()

class Tipos_Elemento(models.Model):
    class Categoria(models.TextChoices):
        ACCESORIOS="Accesorios",_("Accesorios")
        PRODUCTOS="Productos",_("Productos")
    categoria=models.CharField(max_length=20,default=Categoria.ACCESORIOS,choices=Categoria.choices, verbose_name="Categoría")
    subcategoria=models.CharField(max_length=20,null=False,unique=True, verbose_name="Subcategoría")
    def __str__(self) -> str:
        return '%s - %s'%(self.categoria[:3].upper(), self.subcategoria)
    def clean(self):
        self.subcategoria= self.subcategoria.title()
          
class Elemento(models.Model):
    tipo_elemento= models.ForeignKey(Tipos_Elemento,null="False", on_delete=models.SET_NULL, verbose_name="Subcategoría")
    nombre=models.CharField(max_length=25)
    marca= models.ForeignKey(Marca,on_delete=models.SET_NULL, null=True,verbose_name=u"Marca")
    descripcion=models.CharField(max_length=500)
    precio=models.IntegerField(verbose_name="Precio")
    stock_elemento=models.IntegerField(verbose_name="Stock", default=0)
    favorito=models.BooleanField(default=False)
    class Porcentaje_ganancia(models.TextChoices):
        diez= '0.1', _('10%')
        quince= '0.15', _('15%')
        veinte= '0.2', _('20%')
        treinta= '0.3', _('30%')
    porcentaje_ganancia=models.CharField(max_length=10, choices=Porcentaje_ganancia.choices, verbose_name="Porcentaje")
    foto=models.ImageField(upload_to="carrito", null=True, blank=True,default="carrito/casa.png")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s %s'%(self.tipo_elemento,self.nombre)
    def clean(self):
        self.nombre= self.nombre.title()
        
class  Favorito(models.Model):
    favorito=models.BooleanField(default=False)
    class Estado(models.TextChoices):
        ACTIVO='True',_('True')
        INACTIVO='False',_('False')
    def __str__(self) -> str:
        return '%s'%(self.nombre)
        
class Cantidad(models.Model):
    fecha= models.DateField(auto_now=True, verbose_name="Fecha de Registro", help_text=u"MM/DD/AAAA")
    cantidad_agregada=models.IntegerField(default=0)
    cantidad_stock=models.IntegerField(verbose_name="Cantidad")
    producto= models.ForeignKey(Elemento, on_delete=models.SET_NULL, null=True, verbose_name=u"Producto")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s' % (self.cantidad_stock)
  
class Electrodomestico(models.Model):
    nombre=models.CharField(max_length=25)
    marca= models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, verbose_name=u"Marca")
    referencia=models.CharField(max_length=25)
    class Estado(models.TextChoices):
        ACTIVO='Activo',_('Activo')
        INACTIVO='Inactivo',_('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s'%(self.nombre)
    
class Servicio(models.Model):
    electrodomestico= models.ForeignKey(Electrodomestico, on_delete=models.SET_NULL, null=True, verbose_name=u"Electrodomestico")
    diagnostico= models.CharField(max_length=500, blank=False, verbose_name="Diagnostico")
    class TipoServicio(models.TextChoices):
        REPARACION='Reparación', _('Reparación')
        MANTENIMIENTO='Mantenimiento', _('Mantenimiento')
    tiposervicio= models.CharField(max_length=20, choices=TipoServicio.choices, verbose_name="Tipo de Servicio")
    fallas_basicas= models.CharField(max_length=255, blank=False, verbose_name="Falla Basica")
    fecha_entrega=models.DateField(verbose_name="Fecha de Entrega", help_text=u"MM/DD/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='Activo',_('Activo')
        INACTIVO='Inactivo',_('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s'%(self.electrodomestico)
    
class Stock(models.Model):
    fecha= models.DateField(auto_now=True, verbose_name="Fecha de Registro", help_text=u"MM/DD/AAAA")
    stock_agregada=models.IntegerField(verbose_name="Stock Nuevo", default=0)
    stock_stock=models.IntegerField(verbose_name="Stock")
    elemento= models.ForeignKey(Elemento, on_delete=models.SET_NULL, null=True, verbose_name=u"elemento")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s' % (self.stock_stock)  