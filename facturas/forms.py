from tkinter import Widget
from django import forms
from facturas.models import *

class FacturaForm(forms.ModelForm):
    class Meta: 
        model = Factura
        fields = [ 'tipofactura']
        
class DetalleForm(forms.ModelForm):
    class Meta: 
        model = Detalle
        fields = ['elemento','cantidad']



# Servicios David
class DetalleServicioForm(forms.ModelForm):
    class Meta: 
        model = DetalleServicio
        fields = ['servicio', 'elemento', 'cantidad', 'costo']
# Final David servicios