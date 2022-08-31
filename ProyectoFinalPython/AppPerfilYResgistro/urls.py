from django.urls import path

from AppPerfilYResgistro.views import registro, editar_perfil


urlpatterns = [    
 
    path('registro/', registro, name='Registro'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
]
