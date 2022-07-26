from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)  
    message = models.CharField(max_length=500)  
