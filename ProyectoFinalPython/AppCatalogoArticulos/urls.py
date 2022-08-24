from django.urls import path

from AppCatalogoArticulos.views import lista_articulos
from AppCatalogoArticulos.views import detalleArticulo

urlpatterns = [    
 
    path('catalogo/listaArticulos/', lista_articulos, name='Articulos'),
    path('vista-detalle-articulo/<int:id>', detalleArticulo, name="VistaDetalleArticulo"),


]
