from django import forms
from usuarios.models import  Cliente, Proveedor, Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol','tipo_documento','documento','especializacion','Unombre','apellido','celular','correo','ciudad']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','descripcion','direccion','contacto','celular','correo']
                

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['tipocliente','nombre','apellido','celular']
                