from django.urls import path
from facturas.views import factura, factura_creara, tfactura, vfactura,  detalle, factura_estado,detalle_estado
from django.contrib.auth import views as auth_views




urlpatterns = [
        # path('crearfactura/', factura, name='factura-factura'),
        path('factura_crear/', factura_creara, name='factura-crear'),
        path('factura/', tfactura, name='factura-tfactura'),
        path('verfactura/<int:pk>', vfactura, name='factura-verfactura'),
        path('detalle/<int:pk>/', detalle, name='factura-detalle'),
        path('detalle-factura/estado/<int:pk>/<str:estado>/', factura_estado, name='factura_estado'),
        path('detalle-estado/eliminar/<int:pk>/', detalle_estado, name='detalle_eliminar_estado'),
]

 