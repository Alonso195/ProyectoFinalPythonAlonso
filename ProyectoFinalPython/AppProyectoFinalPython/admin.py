from django.contrib import admin

from AppProyectoFinalPython.models import  Cliente, Pedido, Proveedor,Articulo

# Register your models here.
    
class ClientesAdmin(admin.ModelAdmin):
    list_display = [ "Nombre", "Apellidos", "CodigoCliente", "Cuit", "Provincia", "Localidad", "Direccion"]
    search_fields =['Nombre','Apellidos']  


class ProveedorAdmin(admin.ModelAdmin):
    list_display = [ "Nombre", "Apellidos", "CodigoProveedor", "Cuit", "Provincia", "Localidad", "Direccion"]
    search_fields =['Nombre','Apellidos']    


class ArticuloAdmin(admin.ModelAdmin):
    list_display = [ "CodigoArticulo", "Descripcion", "Color", "Talle", "Precio", "CodigoBarra" ]
    search_fields =['CodigoArticulo','Descripcion']    


admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Cliente,ClientesAdmin)
admin.site.register(Pedido)    
admin.site.register(Proveedor, ProveedorAdmin)    
 
