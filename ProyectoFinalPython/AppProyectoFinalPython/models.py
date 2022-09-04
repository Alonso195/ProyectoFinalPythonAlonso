from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)  
    message = models.CharField(max_length=500)  


class Proveedor(models.Model):
    CodigoProveedor = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)  
    Provincia = models.CharField(max_length=500)  
    Localidad = models.CharField(max_length=500)  
    Direccion = models.CharField(max_length=1000)  
    Cuit = models.CharField(max_length=1000)  


    def __str__(self) -> str:
        return f'Nombre: {self.Nombre} {self.Apellidos} - Código Proveedor: {self.CodigoProveedor}'


class Cliente(models.Model):
    CodigoCliente = models.CharField(max_length=8)
    Nombre = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Provincia = models.CharField(max_length=20)
    Localidad = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=30)
    Cuit = models.CharField(max_length=11)
    
    def __str__(self) -> str:
        return f'Nombre: {self.Nombre} {self.Apellidos} - Código Cliente: {self.CodigoCliente}'
 

class Articulo(models.Model):
    CodigoArticulo = models.CharField(max_length=8)
    Descripcion = models.CharField(max_length=30)
    Color = models.CharField(max_length=30)
    Talle = models.CharField(max_length=20)
    Precio = models.CharField(max_length=20)
    CodigoBarra = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='articulos', blank=True, null=True)
    DescripcionLarga = models.CharField(max_length=300)
        
    def __str__(self) -> str:
        return f'Codigo: {self.CodigoArticulo} - Descripcion: {self.Descripcion}'


#---------------------------------------------------
class Pedido(models.Model):
    Numpedido = models.IntegerField()
    Fecha = models.DateField()
    CodClie = models.CharField(max_length=8)       

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True) 