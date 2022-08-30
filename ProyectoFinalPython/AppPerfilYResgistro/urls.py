from django.urls import path

from AppPerfilYResgistro.views import registro


urlpatterns = [    
 
    path('registro/', registro, name='Registro'),


]
