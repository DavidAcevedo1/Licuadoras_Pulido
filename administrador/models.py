from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Usuario(models.Model):
    documento=models.CharField(unique=True,max_length=10)
    class TipoDoc(models.TextChoices):
        CEDULA='C.C.', _('Cedula')
        TARJETA='T.I.', _('Tarjeta')
        REGISTRO='R.C.', _('Registro Civil')
        EXTRANJERIA='C.E.', _('Cedula Extranjeria')
    tipodoc= models.CharField(max_length=20, choices=TipoDoc.choices, verbose_name="Tipo de documento")
    class Rol(models.TextChoices):
        ADMINISTRADOR='Administrador', _('Administrador')
        TRABAJADOR='Trabajador', _('Trabajador')
        PROVEEDOR='Proveedor', _('Proveedor')
        CLIENTE='Cliente', _('Cliente')
    rol= models.CharField(max_length=20, choices=Rol.choices, verbose_name="Rol")
    nombre= models.CharField(max_length=30, blank=False, verbose_name="Nombre")
    apellido= models.CharField (max_length=30, blank=False, verbose_name="Apellido")
    telefono= PhoneNumberField()
    direccion= models.CharField(max_length=30)
    correo= models.EmailField( max_length=25)
    especializacion= models.CharField(max_length=50)
    contraseña= models.CharField(blank=False, null=False, max_length=20)
    ciudad= models.CharField(max_length=50)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s %s' %( self.nombre, self.apellido)
    def clean(self):
        self.nombre= self.nombre.title()
        self.apellido= self.apellido.title()
        
    
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
    stock=models.IntegerField()
    nombre=models.CharField(max_length=25)
    marca= models.ForeignKey(Marca,on_delete=models.SET_NULL, null=True,verbose_name=u"Marca")
    descripcion=models.CharField(max_length=500)
    precio=models.IntegerField(verbose_name="Precio")
    favorito=models.BooleanField(default=False)
    class Porcentaje_ganancia(models.TextChoices):
        diez= '0.1', _('10%')
        quince= '0.15', _('15%')
        veinte= '0.2', _('20%')
        treinta= '0.3', _('30%')
    porcentaje_ganancia=models.CharField(max_length=10, choices=Porcentaje_ganancia.choices, verbose_name="Porcentaje")
    foto=models.ImageField(upload_to="carrito", null=True, blank=True,default="carrito/casa.png")
    class Estado(models.TextChoices):
        ACTIVO='Activo',_('Activo')
        INACTIVO='Inactivo',_('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s'%(self.nombre)
    def clean(self):
        self.nombre= self.nombre.title()

class Factura(models.Model):
    elemento= models.ForeignKey(Elemento,on_delete=models.SET_NULL, null=True,verbose_name=u"Elemento")
    cantidad= models.IntegerField()
    class CompraoVenta(models.TextChoices):
        COMPRA='Compra', _('Compra')
        VENTA='Venta', _('Venta')
    compraoventa= models.CharField(max_length=6, choices=CompraoVenta.choices, verbose_name="CompraoVenta")
    usuario= models.ForeignKey(Usuario,on_delete=models.SET_NULL, null=True,verbose_name=u"Usuario")
    monto=models.IntegerField()
    fecha= models.DateField(verbose_name="Fecha de Registro", help_text=u"MM/DD/AAAA")
    class Estado(models.TextChoices):
        PAGADO='Pagado',_('Pagado')
        ANULADO='Anulado',_('Anulado')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.PAGADO)
    def __str__(self) -> str:
        return '%s '%(self.elemento)
  
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
    cantidad= models.IntegerField()
    fallas_basicas= models.CharField(max_length=255, blank=False, verbose_name="Falla Basica")
    fecha_entrega=models.DateField(verbose_name="Fecha de Entrega", help_text=u"MM/DD/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='Activo',_('Activo')
        INACTIVO='Inactivo',_('Inactivo')
    estado= models.CharField(max_length=20, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def __str__(self) -> str:
        return '%s'%(self.electrodomestico)
   