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
