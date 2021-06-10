from django.db import models
from authentication_service.authentication.models import User


class Type(models.Model):
    TYPE = (
        ('poupanca', 'Conta Poupança'),
        ('corrente', 'Conta Corrente'),
        ('salario', 'Conta Salário')
    )

    type = models.CharField(max_length=50, choices=TYPE, null=False)

    def __str__(self):
        return f"{self.type}"


class Account(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=10)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)


class LoanCredit(models.Model):
    credit = models.DecimalField(max_digits=18, decimal_places=10)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)


class Card (models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expire_date = models.DateField(blank=False)
    cvv = models.CharField(max_length=3)
    password = models.PositiveIntegerField(max_length=4, blank=False, null=False)
    has_debit = models.BooleanField(default=False)
    has_credit = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    account = models.Model(Account, on_delete=models.PROTECT)
