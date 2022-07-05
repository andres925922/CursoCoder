from django.db import models
from .model_base import Base_Model, Estado

class Manufacturer_Mixin(Base_Model, Estado):
    name = models.CharField(max_length = 10, null=False, unique=True)