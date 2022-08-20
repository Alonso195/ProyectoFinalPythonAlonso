from django.urls import path

from AppProyectoFinalPython.views import inicio, contactUs, buscarProveedor, login_request, acercaDeMi
from AppProyectoFinalPython.views import ProveedorCreate, ProveedorDelete, ProveedorDetail, ProveedorList, ProveedorUpdate,ClienteCreate, ClienteDelete, ClienteDetail, ClienteUpdate,ClienteList,ArticuloList,ArticuloDetail,ArticuloCreate,ArticuloUpdate,ArticuloDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path('', inicio, name='Inicio'),
    path('acercaDeMi', acercaDeMi, name='AcercaDeMi'),

    path('contacto/', contactUs, name='Contacto'),  
    path('buscarProveedor/', buscarProveedor, name='BuscarProveedor'),  

    path('listaProveedores/', ProveedorList.as_view(), name="ListaProveedores"),
    path('detalleProveedores/<int:pk>', ProveedorDetail.as_view(), name="DetalleProveedores"),
    path('creaProveedores/', ProveedorCreate.as_view(), name="CreaProveedores"),    
    path('actualizaProveedores/<int:pk>', ProveedorUpdate.as_view(), name="ActualizaProveedores"),
    path('eliminaProveedores/<int:pk>', ProveedorDelete.as_view(), name="EliminaProveedores"),

    path('listaClientes/', ClienteList.as_view(), name="ListaClientes"),
    path('detalleClientes/<int:pk>', ClienteDetail.as_view(), name="DetalleClientes"),
    path('creaClientes/', ClienteCreate.as_view(), name="CreaClientes"),    
    path('actualizaClientes/<int:pk>', ClienteUpdate.as_view(), name="ActualizaClientes"),
    path('eliminaClientes/<int:pk>', ClienteDelete.as_view(), name="EliminaClientes"),

    path('listaArticulos/', ArticuloList.as_view(), name="ListaArticulos"),
    path('detalleArticulos/<int:pk>', ArticuloDetail.as_view(), name="DetalleArticulos"),
    path('creaArticulos/', ArticuloCreate.as_view(), name="CreaArticulos"),    
    path('actualizaArticulos/<int:pk>', ArticuloUpdate.as_view(), name="ActualizaArticulos"),
    path('eliminaArticulos/<int:pk>', ArticuloDelete.as_view(), name="EliminaArticulos"),

    path('Login', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),


]
