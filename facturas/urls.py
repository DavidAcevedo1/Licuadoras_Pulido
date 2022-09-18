from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from facturas.views import factura,tfactura,vfactura,detalle,detalle_estado,factura_estado,factura_eliminar



from facturas.views import *
urlpatterns = [
        path('crearfactura/',login_required (factura), name='factura-factura'),
        path('factura/', login_required(tfactura), name='factura-tfactura'),
        path('verfactura/<int:pk>',login_required (vfactura), name='factura-verfactura'),
        path('detalle/<int:pk>/',login_required (detalle), name='factura-detalle'),
        # path('detalle/<int:pk>/',login_required (detalle), name='factura-detalle-servicio'),
        path('detalle-factura/estado/<int:pk>/<str:estado>/',login_required (factura_estado), name='factura-estado'),
        path('detalle-estado/eliminar/<int:pk>/',login_required (detalle_estado), name='detalle-estado-eliminar'),
        path('factura-eliminar/<int:pk>/', factura_eliminar, name='factura-eliminar'),
        # path('categoria/d/<int:pk>/', tipoelemento_eliminar, name='administrador-categoria-eliminar'),
]

        #path('categoria/d/<int:pk>/', tipoelemento_eliminar, name='administrador-categoria-eliminar'),

