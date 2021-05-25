from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=10)
    owner_id = models.IntegerField(unique=True)

# account = Account(1, "05846", 657, 1)
# account.save()
