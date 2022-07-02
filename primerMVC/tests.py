from django.test import TestCase
from .models import Familiar

# Create your tests here.

FAMILIARES = None

def create_familiares():
    andres = Familiar(nombre = "Luis Andres", apellido = "Convertini", edad = 31)
    luciana = Familiar(nombre = "Luciana", apellido = "Becerra", edad = 28)
    muchacho = Familiar(nombre = "Muchacho", apellido = "El perro", edad = 1)

    andres.save()
    luciana.save()
    muchacho.save()

def get_familiares():
    global FAMILIARES
    FAMILIARES = Familiar.objects.all()