from django.db import models


class Users(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=32, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)

