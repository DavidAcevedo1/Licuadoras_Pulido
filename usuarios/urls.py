from django.urls import path
from django.contrib.auth.decorators import login_required
from usuarios.views import *

urlpatterns = [
    #Pestañas de usuarios
    path('accesorios/', accesorio, name='usuarios-accesorios'),
    path('productos/', producto, name='usuarios-productos'),
    path('nosotros/', nosotros, name='usuarios-nosotros'),
    path('serviciocliente/', serviciocliente, name='usuarios-servicios'),
    path('carrito/', carrito, name='usuarios-carrito'),
    path('politicas/', politicasprivacidad, name='usuarios-politicas'),
    
    #Registro usuarios
    path('crearusuario/',login_required (cusuario), name='usuario-crearUsuario'),
    path('tablausuario/', login_required (tusuario), name='usuario-tablaUsuario'),
    path('verusuario/<int:pk>', login_required (vusuario), name='usuario-verusuario'),
    path('editarusuario/<int:pk>', login_required (Editarusuario), name='usuario-editarusuario'),
    path('tablausuario/eliminar/<int:pk>/', login_required (usuario_eliminar), name='usuario-usuario-eliminar'),

    #carrito
    path('agregar/<int:elemento_id>/', agregar_elemento, name="agregar"),
    path('eliminar/<int:elemento_id>/', eliminar_elemento, name="eliminar"),
    path('restar/<int:elemento_id>/', restar_elemento, name="restar"),
    path('limpiar/',limpiar_carrito, name="limpiar"),
    path('detalle/<int:pk>/<str:url_back>/', detalle, name="detalle")
]