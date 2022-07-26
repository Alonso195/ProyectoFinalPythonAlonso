from django.urls import path
from AppProyectoFinalPython.views import inicio, contactUs

urlpatterns = [    
    path('', inicio, name='Inicio'),
    path('contacto/', contactUs, name='Contacto'),

]
