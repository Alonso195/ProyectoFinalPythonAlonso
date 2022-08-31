from django.urls import path

from AppPerfilYResgistro.views import registro, editar_perfil, agregar_avatar


urlpatterns = [    
 
    path('registro/', registro, name='Registro'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
    path('editar-avatar/', agregar_avatar, name='EditarAvatar'),

]
