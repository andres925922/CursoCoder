from os import system
from django.db import models

# Create your models here.

class Base(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    modification_date = models.DateTimeField(auto_now=True, null=False)

class Familiar(Base):
    nombre = models.CharField(max_length=80, null=False)
    apellido = models.CharField(max_length=80, null=False)
    edad = models.IntegerField(null=False)

