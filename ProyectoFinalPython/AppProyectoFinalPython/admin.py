from django.contrib import admin

from AppProyectoFinalPython.models import Articulos, Cliente, Pedido, Proveedor

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['CodClie','NombreyApellido','Provincia','Localidad','Direccion','Cuit']
    search_fields =['CodClie','NombreyApellido']
    
class ProveedorAdmin(admin.ModelAdmin):
    list_display = [ "Nombre", "Apellidos", "CodigoProveedor", "Cuit", "Provincia", "Localidad", "Direccion"]
    search_fields =['Nombre','Apellidos']    

admin.site.register(Articulos)
admin.site.register(Cliente,ClientesAdmin)
admin.site.register(Pedido)    
admin.site.register(Proveedor, ProveedorAdmin)    
 
