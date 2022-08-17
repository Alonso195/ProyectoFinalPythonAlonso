from django.urls import path

from AppCatalogoArticulos.views import lista_articulos

urlpatterns = [    
 
    path('catalogo/listaArticulos/', lista_articulos, name='Articulos'),


]
