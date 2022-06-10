from django.urls import path
from administrador.views import copiaseguridad, electrodomestico, electrodomestico_editar, electrodomestico_eliminar, elemento, elemento_editar, elemento_eliminar, factura, factura_eliminar, inicioadmin, marca, marca_editar, marca_eliminar, servicio, servicio_editar, servicio_eliminar, tipoelemento, tipoelemento_editar, tipoelemento_eliminar, usuario, usuario_editar, usuario_eliminar,stock

urlpatterns = [
    path('inicioadmin/', inicioadmin, name='administrador-inicioadmin'),
    
    path('usuario/', usuario, name='administrador-usuario'),
    path('usuario/u/<int:pk>/', usuario_editar, name='administrador-usuario-editar'),
 
    
    path('categoria/', tipoelemento, name='administrador-categoria'),
    path('categoria/u/<int:pk>/', tipoelemento_editar, name='administrador-categoria-editar'),
    path('categoria/d/<int:pk>/', tipoelemento_eliminar, name='administrador-categoria-eliminar'),
    
    path('elemento/', elemento, name='administrador-elemento'),
    path('elemento/u/<int:pk>/', elemento_editar, name='administrador-elemento-editar'),
    path('elemento/d/<int:pk>/', elemento_eliminar, name='administrador-elemento-eliminar'),
    
    path('marca/', marca, name='administrador-marca'),
    path('marca/u/<int:pk>/', marca_editar, name='administrador-marca-editar'),
    path('marca/d/<int:pk>/', marca_eliminar, name='administrador-marca-eliminar'),
    
    path('factura/', factura, name='administrador-factura'),
    path('factura/d/<int:pk>/', factura_eliminar, name='administrador-factura-eliminar'),
    
    path('electrodomestico/', electrodomestico, name='administrador-electrodomestico'),
    path('electrodomestico/u/<int:pk>/', electrodomestico_editar, name='administrador-electrodomestico-editar'),
    path('electrodomestico/d/<int:pk>/', electrodomestico_eliminar, name='administrador-electrodomestico-eliminar'),
    
    path('servicio/', servicio, name='administrador-servicio'),
    path('servicio/u/<int:pk>/', servicio_editar, name='administrador-servicio-editar'),
    path('servicio/d/<int:pk>/', servicio_eliminar, name='administrador-servicio-eliminar'),
    
    path('copiaseguridad/', copiaseguridad, name='administrador-copiaseguridad'),
    path('stock/l/<int:pk>', stock ,name='elemento-stock')
]