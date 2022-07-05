from django.db import models

# Create your models here.


class Base_Model(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    modification_date = models.DateTimeField(auto_now=True, null=False)

class Estado(models.Model):
    deleted = models.BooleanField(default=False)