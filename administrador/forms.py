from dataclasses import field
from django import forms
from administrador.models import Electrodomestico,Elemento, Marca, Servicio, Tipos_Elemento


class TipoElementoForm(forms.ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class TipoElementoEditarForm(forms.ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class ElementoForm(forms.ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','stock','nombre','marca','descripcion','precio','porcentaje_ganancia', 'foto']

class ElementoEditarForm(forms.ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','stock','nombre','marca' ,'descripcion','precio','porcentaje_ganancia', 'foto']
                
class MarcaForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']
        
class MarcaEditarForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']
        
class ElectrodomesticoForm(forms.ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']

class ElectrodomesticoEditarForm(forms.ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields=['electrodomestico','diagnostico', 'tiposervicio', 'cantidad', 'fallas_basicas','fecha_entrega']

class ServicioEditarForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields=['electrodomestico','diagnostico', 'tiposervicio', 'cantidad', 'fallas_basicas','fecha_entrega']
