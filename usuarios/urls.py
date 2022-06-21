from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import Editarusuario, agregar_elemento, carrito, cliente, cliente_crear, cusuario, eliminar_elemento,inicio, accesorio, limpiar_carrito, politicasprivacidad, producto, proveedor, proveedor_crear, restar_elemento, serviciocliente, nosotros, tusuario, usuario_crear, usuario_eliminar, vusuario

urlpatterns = [
    path('inicio/', inicio, name='usuarios-inicio'),
    path('accesorios/', accesorio, name='usuarios-accesorios'),
    path('productos/', producto, name='usuarios-productos'),
    path('serviciocliente/', serviciocliente, name='usuarios-servicios'),
    path('nosotros/', nosotros, name='usuarios-nosotros'),
    path('carrito/', carrito, name='usuarios-carrito'),
    path('politicas/', politicasprivacidad, name='usuarios-politicas'),
    
    #usuario
    # path('crearusuario/', cusuario, name='usuario-crearUsuario'),
    path('usuario_crear/', usuario_crear, name='usuario-crear'),
    path('tablausuario/', tusuario, name='usuario-tablaUsuario'),
    path('verusuario/<int:pk>', vusuario, name='usuario-verusuario'),
    path('editarusuario/<int:pk>', Editarusuario, name='usuario-editarusuario'),
    path('tablausuario/eliminar/<int:pk>/', usuario_eliminar, name='usuario-usuario-eliminar'),
    
    #proveedor
    path('proveedor_crear/', proveedor_crear, name='proveedor-crear'),
    path('proveedor/', proveedor, name='usuario-proveedor'),
    # path('elemento/u/<int:pk>/', elemento_editar, name='administrador-elemento-editar'),
    # path('elemento/d/<int:pk>/', elemento_eliminar, name='administrador-elemento-eliminar'),
    
    #cliente
    path('cliente_crear/', cliente_crear, name='cliente-crear'),
    path('cliente/', cliente, name='usuario-cliente'),
    
    
    #carrito
    path('agregar/<int:elemento_id>/', agregar_elemento, name="agregar"),
    path('eliminar/<int:elemento_id>/', eliminar_elemento, name="eliminar"),
    path('restar/<int:elemento_id>/', restar_elemento, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
