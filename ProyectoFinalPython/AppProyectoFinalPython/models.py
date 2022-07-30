from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)  
    message = models.CharField(max_length=500)  


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)  
    date = models.DateField()  



class Author(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)    
    born = models.DateField()  


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
