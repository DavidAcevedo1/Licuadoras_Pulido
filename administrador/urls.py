from django.urls import path
from administrador.models import Favorito
from django.contrib.auth.decorators import login_required
from administrador.views import *

urlpatterns = [
    path('inicioadmin/',login_required (inicioadmin), name='administrador-inicioadmin'),

    path('categoria/',login_required (tipoelemento), name='administrador-categoria'),
    path('categoria/u/<int:pk>/',login_required (tipoelemento_editar), name='administrador-categoria-editar'),
    path('categoria/d/<int:pk>/',login_required (tipoelemento_eliminar), name='administrador-categoria-eliminar'),
    
    path('marca/', login_required(marca), name='administrador-marca'),
    path('marca/u/<int:pk>/',login_required (marca_editar), name='administrador-marca-editar'),
    path('marca/d/<int:pk>/',login_required(marca_eliminar), name='administrador-marca-eliminar'),
    
    path('elemento/', login_required(elemento), name='administrador-elemento'),
    path('elemento/u/<int:pk>/',login_required (elemento_editar), name='administrador-elemento-editar'),
    path('elemento/d/<int:pk>/',login_required (elemento_eliminar), name='administrador-elemento-eliminar'),
    
    path('electrodomestico/', electrodomestico, name='administrador-electrodomestico'),
    path('electrodomestico/u/<int:pk>/',login_required (electrodomestico_editar), name='administrador-electrodomestico-editar'),
    path('electrodomestico/d/<int:pk>/',login_required (electrodomestico_eliminar), name='administrador-electrodomestico-eliminar'),
    path('electrodomestico/f/<int:pk>/', login_required(electrodomestico_favorito), name='administrador-electrodomestico-favorito'),
    
    path('servicio/',login_required (servicio), name='administrador-servicio'),
    path('servicio/u/<int:pk>/',login_required (servicio_editar), name='administrador-servicio-editar'),
    path('servicio/d/<int:pk>/',login_required (servicio_eliminar), name='administrador-servicio-eliminar'),
    
    path('copiaseguridad/<str:tipo>/',login_required  (copiaseguridad), name='administrador-copiaseguridad'),
]