"""prueba URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from catastro_equipos.urls import products_patterns
from phone.urls import phones_patterns
from usuarios.urls import users_patterns
from asignacion.urls import asignation_patterns
from accesorios.urls import accesorios_patterns
from django.conf import settings
from catastro_equipos import views 
from .views import SignUpView, error_404_page
from catastro_equipos.views import HomePageView

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('system/', admin.site.urls),
    path('products/', include(products_patterns)),
    path('phones/', include(phones_patterns)),
    path('user/', include(users_patterns)),
    path('asignation/', include(asignation_patterns)),
    path('accesorios/', include(accesorios_patterns)),
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Administración de Equipos BCN'
admin.site.index_title = 'BCN School'
admin.site.site_title = 'Administrador BCN'
admin.site.site_name = 'Administración BCN School'   

handler404 = 'prueba.views.error_404_page' 