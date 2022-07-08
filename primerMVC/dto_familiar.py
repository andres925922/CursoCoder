from datetime import datetime

from primerMVC.models import Familiar

class DTO_Familiar:
    id: int = None
    creation_date: datetime = None
    modification_date: datetime = None
    nombre: str = None
    apellido: str = None
    edad: int = None


class DTO_Familiar_New:
    def __init__(self, **kargs) -> None:
        self.id: int = kargs.get("x")["id"]
        self.nombre: str = kargs.get("x")["nombre"]
        self.apellido: str = kargs.get("x")["apellido"]
        self.edad: int = kargs.get("x")["edad"]

    def __getitem__(self, key):
        """ Función que nos permite getear los datos como si fuera un diccionario """
        return self.__dict__[key]
