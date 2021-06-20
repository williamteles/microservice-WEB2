from django.db import models


class Account(models.Model):
    TYPE = (
        ('poupanca', 'Conta Poupança'),
        ('corrente', 'Conta Corrente'),
        ('salario', 'Conta Salário')
    )

    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=2)
    owner_id = models.IntegerField(unique=True)
    type_account = models.CharField(max_length=50, choices=TYPE)


class Card(models.Model):
    card_number = models.CharField(max_length=19, unique=True)
    expire_date = models.DateField(blank=False)
    cvv = models.CharField(max_length=3)
    password = models.PositiveIntegerField(blank=False, null=False)
    has_debit = models.BooleanField(default=True)
    has_credit = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    bill = models.DecimalField(max_digits=18, decimal_places=2)
    limit = models.DecimalField(max_digits=18, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

   
class Transactions(models.Model):
    CATEGORIES = (
        ('Restaurante', 'Restaurante'),
        ('Transporte', 'Transporte'),
        ('Serviços', 'Serviços'),
        ('Supermercado', 'Supermercado'),
        ('Lazer', 'Lazer'),
        ('Educação', 'Educação'),
        ('Eletrônicos', 'Eletrônicos'),
        ('Saúde', 'Saúde'),
        ('Casa', 'Casa'),
        ('Outros', 'Outros')
    )

    TYPE = (
        ('Depósito', 'Depósito'),
        ('Pagamento', 'Pagamento'),
        ('Transferência', 'Transferência'),
        ('Compra', 'Compra')
    )

    PAYMENT_TYPE = (
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito')
    )

    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    value = models.DecimalField(max_digits=18, decimal_places=2)
    parcelas = models.PositiveIntegerField(default=1)
    categories = models.CharField(max_length=50, choices=CATEGORIES, null=True, blank=True)
    type_transaction = models.CharField(max_length=50, choices=TYPE)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE, null=True, blank=True)
    transfer_account = models.PositiveIntegerField(null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
