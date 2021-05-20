from django.db import models

# Create your models here.
class Account(models.Model):
    number_account = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    id_owner = models.IntegerField(unique=True)

# account = Account(number_account = '04',balance = 200, id_owner = 2)
# account.save()
