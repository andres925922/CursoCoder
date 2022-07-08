from .models import Familiar
from .dto_familiar import DTO_Familiar, DTO_Familiar_New
from typing import List

def get_all_familiares():
    """ retorna listado de familiares 
    """
    #  -> List[DTO_Familiar]
    return Familiar.objects.all()

def get_all_familiares_new() -> List[DTO_Familiar_New]:
    """ retorna listado de familiares serializados mediante DTO
    """
    #  -> List[DTO_Familiar]
    return [DTO_Familiar_New(x = x) for x in Familiar.objects.all().values()]
