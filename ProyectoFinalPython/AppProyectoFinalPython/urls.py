from django.urls import path
from AppProyectoFinalPython.views import inicio, contactUs, books, authors
from AppProyectoFinalPython.views import ProveedorCreate, ProveedorDelete, ProveedorDetail, ProveedorList, ProveedorUpdate

urlpatterns = [    
    path('', inicio, name='Inicio'),
    path('contacto/', contactUs, name='Contacto'),
    path('libros/', books, name='Libro'),
    path('Autores/', authors, name='Autores'),

    path('listaProveedores/', ProveedorList.as_view(), name="ListaProveedores"),
    path('detalleProveedores/<int:pk>', ProveedorDetail.as_view(), name="DetalleProveedores"),
    path('creaProveedores', ProveedorCreate.as_view(), name="CreaProveedores"),
    #path('creaProveedores/', CrearProveedor, name="CreaProveedores"),
    path('actualizaProveedores/<int:pk>', ProveedorUpdate.as_view(), name="ActualizaProveedores"),
    path('eliminaProveedores/<int:pk>', ProveedorDelete.as_view(), name="EliminaProveedores"),


]
