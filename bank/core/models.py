from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import Value

# Create your models here.
class Account(models.Model):
    number_account = models.CharField(max_length=10,primary_key=True,null=False)
    value = models.DecimalField(max_digits=10,decimal_places=2)

    