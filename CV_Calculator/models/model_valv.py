from .model_base import Base_Model, Estado
from model_manuf import Manufacturer_Mixin
from django.db import models


class Valve_Category_Mixin(Base_Model, Estado):
    cat_name = models.CharField(max_length = 10, unique=True)
    cat_desc = models.CharField(max_length = 10, null=False)
    
    def __str__(self):
        return "Valve_Category"

class Valve_Mixin(Base_Model, Estado):
    category = models.ForeignKey(Valve_Category_Mixin, on_delete=models.PROTECT)
    manuf = models.ForeignKey(Manufacturer_Mixin, on_delete=models.PROTECT)
    description = models.CharField(max_length=50, null=False)
    extended_description = models.CharField(max_length=150)
    cv = models.FloatField(db_index=True, max_length=3, null=False)

    def __str__(self):
        return "Valves"