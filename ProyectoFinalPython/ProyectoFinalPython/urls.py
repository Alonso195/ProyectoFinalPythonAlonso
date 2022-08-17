

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppProyectoFinalPython.urls')),
    path('', include('AppCatalogoArticulos.urls')),
    path('', include('AppPerfilYResgistro.urls')),
]
