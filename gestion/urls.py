"""gestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from gestion.views import inicio, login, password_reset, contraseña_email, contraseña_correo, contraseña_confirmar
from administrador.views import inicioadmin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('inicio-ad/', inicioadmin, name="inicioadmin"),
    path('', include('administrador.urls')),
    path('', include('usuarios.urls')),
    # Logueo
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
    # Recuperación
    path('reset/password_reset', password_reset, {'template_name':'recuperacion/contraseña-correo.html',
        'email_template':'recuperacion/contraseña-email.html'},
        name='password_reset'),
    path('reset/contraseña-correo', contraseña_correo, {'template_name':'recuperacion/contraseña-correo.html',},
        name='contraseña-correo'),
    path('reset/(?P<uidb64>[0-9A-z_\-]+)/(?P<token>.+)/$', contraseña_confirmar, {'template_name':'recuperacion/contraseña-confirmar.html',},
        name='contraseña-confirmar'),
    # path('reset/done', contraseña_confirmar, {'template_name':'recuperacion/contraseña-correo.html',},
    #     name='contraseña-correo'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
