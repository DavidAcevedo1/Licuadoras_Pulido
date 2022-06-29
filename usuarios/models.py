from django.db import models
from django.utils.translation import gettext_lazy as _


# class Rol(models.Model):
#     Rid=models.AutoField(primary_key=True)
#     Rnombre=models.CharField(max_length=12)
#     class Meta:
#         db_table="usuarios_rol"
#     def __str__(self) -> str:
#         return "%s "% (self.Rnombre)
    
    
class Usuario(models.Model):
    Uid=models.AutoField(primary_key=True)
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Proveedor='Proveedor', _('Proveedor')
        Trabajador='Trabajador', _('Trabajador')
        Cliente='Cliente', _('Cliente')
    rol= models.CharField(max_length=13,null=True, choices=Rol.choices, verbose_name="rol")  
    especializacion=models.CharField(null=True,max_length=20)
    Unombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    documento=models.CharField(unique=True,max_length=10)
    celular=models.CharField(unique=True,max_length=10)
    correo=models.EmailField(unique=True,null=True,max_length=20)
    ciudad=models.CharField(null=True,max_length=20)
    class Tipo_documento(models.TextChoices):
        Cedula_ciudadania='C.C', _('C.C')
        Tarjeta_identidad='T.I', _('T.I')
        Cedula_extranjeria='C.E', _('C.E')
    tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")  
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    class Meta:
        db_table="usuarios_usuario"
    def __str__(self) -> str:
        return "%s "% (self.Unombre)
    def clean(self):
        self.nombre= self.Unombre.title()
        
        
class Cliente(models.Model):
    class TipoCliente(models.TextChoices):
        NAT='Natural', _('Natural')
        JUR='Juridica', _('Juridica')
    tipocliente= models.CharField(max_length=10,default='Natural', choices=TipoCliente.choices, verbose_name="Tipo decliente")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        super(Cliente, self).save()
        
    class Meta:
        verbose_name_plural = "Clientes"


class Proveedor(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    descripcion=models.CharField(max_length=250,null=True, blank=True)
    direccion=models.CharField(max_length=200,null=True, blank=True)
    contacto=models.CharField(max_length=100)
    celular=models.CharField(max_length=10,null=True, blank=True)
    correo=models.CharField(max_length=250,null=True,blank=True)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Proveedor, self).save()    
        
    class Meta:
        verbose_name_plural = "Proveedores"
    
    
    
# class Uadministrador(models.Model):
#     class Rol(models.TextChoices):
#         Administrador='Administrador', _('Administrador')
#         Proveedor='Proveedor', _('Proveedor')
#         Asociada='Asociada', _('Asociada')
#         Cliente='Cliente', _('Cliente')
#     rol= models.CharField(max_length=13, choices=Rol.choices, verbose_name="rol")  
#     nombre=models.CharField(max_length=50, verbose_name="Nombre")
#     apellido=models.CharField(max_length=50, verbose_name="Apellido")
#     documento=models.CharField(unique=True,max_length=10)
#     celular=models.CharField(unique=True,max_length=10)
#     class Tipo_documento(models.TextChoices):
#         Cedula_ciudadania='C.C', _('C.C')
#         Tarjeta_identidad='T.I', _('T.I')
#         Cedula_extranjeria='C.E', _('C.E')
#     tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")
    
#     def __str__(self) -> str:
#         return "%s"% (self.nombre, self.apellido)
#     def clean(self):
#         self.nombre= self.nombre.capitalize()
#         self.apellido= self.apellido.capitalize()
        
