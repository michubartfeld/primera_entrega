from unittest.util import _MAX_LENGTH
from django.db import models

class Comprador(models.Model):
    email= models.EmailField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)

class Stock(models.Model):
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    cantidad = models.IntegerField() 

class Vendedor(models.Model):
    email= models.EmailField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
