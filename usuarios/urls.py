from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from usuarios.views import Editarusuario, agregar_elemento, carrito, cusuario, detalle, eliminar_elemento, accesorio, limpiar_carrito, politicasprivacidad, producto, restar_elemento, serviciocliente, nosotros, tusuario, usuario_eliminar, vusuario

urlpatterns = [
    path('accesorios/',login_required (accesorio), name='usuarios-accesorios'),
    path('productos/',login_required (producto), name='usuarios-productos'),
    path('serviciocliente/',login_required (serviciocliente), name='usuarios-servicios'),
    path('nosotros/',login_required (nosotros), name='usuarios-nosotros'),
    path('carrito/',login_required (carrito), name='usuarios-carrito'),
    path('politicas/',login_required (politicasprivacidad), name='usuarios-politicas'),
    
    #usuarios
    path('crearusuario/',login_required (cusuario), name='usuario-crearUsuario'),
    path('tablausuario/', login_required(tusuario), name='usuario-tablaUsuario'),
    path('verusuario/<int:pk>',login_required (vusuario), name='usuario-verusuario'),
    path('editarusuario/<int:pk>',login_required (Editarusuario), name='usuario-editarusuario'),
    path('tablausuario/eliminar/<int:pk>/',login_required (usuario_eliminar), name='usuario-usuario-eliminar'),
    
    #carrito
    path('agregar/<int:elemento_id>/',login_required (agregar_elemento), name="agregar"),
    path('eliminar/<int:elemento_id>/',login_required (eliminar_elemento), name="eliminar"),
    path('restar/<int:elemento_id>/',login_required (restar_elemento), name="restar"),
    path('limpiar/',login_required (limpiar_carrito), name="limpiar"),
    path('detalle/<int:pk>/<str:url_back>/',login_required (detalle), name="detalle")
]