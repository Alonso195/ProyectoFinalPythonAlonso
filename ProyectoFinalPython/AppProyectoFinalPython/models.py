from django.db import models

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


class Articulos(models.Model):
    CodItm = models.CharField(max_length=8, unique=True) # se hace unique para que sea codigo unico
    Descripcion = models.CharField(max_length=20)
    DiasGarantia = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.CodItm} - {self.Descripcion}'
    class Meta():
        verbose_name_plural = 'Articulos'
        ordering = ('Descripcion','-CodItm') # desciendiente por coditm
        unique_together = ('CodItm', 'Descripcion') # de esta forma nose puden repetir ni nombre ni descricopnm ala vez


class Cliente(models.Model):
    CodClie = models.CharField(max_length=8)
    NombreyApellido = models.CharField(max_length=30)
    Provincia = models.CharField(max_length=20)
    Localidad = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=30)
    Cuit = models.CharField(max_length=11)
    
    def __str__(self) -> str:
        return f'{self.CodClie} - {self.NombreyApellido}'
 

class Pedido(models.Model):
    Numpedido = models.IntegerField()
    Fecha = models.DateField()
    CodClie = models.CharField(max_length=8)        
