from .models import Familiar
from .dto_familiar import DTO_Familiar
from typing import List

def get_all_familiares() -> List[DTO_Familiar]:
    """ retorna listado de familiares 
    """
    return Familiar.objects.all()