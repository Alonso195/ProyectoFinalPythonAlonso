from django.urls import path
from AppProyectoFinalPython.views import inicio, contactUs, books, authors

urlpatterns = [    
    path('', inicio, name='Inicio'),
    path('contacto/', contactUs, name='Contacto'),
    path('libros/', books, name='Libro'),
    path('Autores/', authors, name='Autores'),



]
