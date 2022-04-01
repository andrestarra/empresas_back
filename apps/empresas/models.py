from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=50)
    nit = models.CharField(max_length=25, unique=True)
    telefono = models.CharField(max_length=15)
