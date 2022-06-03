from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import agregar_elemento, carrito, eliminar_elemento,inicio, accesorio, limpiar_carrito, politicasprivacidad, producto, restar_elemento, serviciocliente, nosotros

urlpatterns = [
    path('inicio/', inicio, name='usuarios-inicio'),
    path('accesorios/', accesorio, name='usuarios-accesorios'),
    path('productos/', producto, name='usuarios-productos'),
    path('serviciocliente/', serviciocliente, name='usuarios-servicios'),
    path('nosotros/', nosotros, name='usuarios-nosotros'),
    path('carrito/', carrito, name='usuarios-carrito'),
    path('politicas/', politicasprivacidad, name='usuarios-politicas'),
    #carrito
    path('agregar/<int:elemento_id>/', agregar_elemento, name="agregar"),
    path('eliminar/<int:elemento_id>/', eliminar_elemento, name="eliminar"),
    path('restar/<int:elemento_id>/', restar_elemento, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
