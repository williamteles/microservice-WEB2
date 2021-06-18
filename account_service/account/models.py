from django.db import models


class Account(models.Model):
    TYPE = (
        ('poupanca', 'Conta Poupança'),
        ('corrente', 'Conta Corrente'),
        ('salario', 'Conta Salário')
    )

    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=10)
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
    bill = models.DecimalField(max_digits=18, decimal_places=10)
    limit = models.DecimalField(max_digits=18, decimal_places=10)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

   
class Transactions(models.Model):
    CATEGORIES = (
        ('restaurante', 'Restaurante'),
        ('transporte', 'Transporte'),
        ('servicos', 'Serviços'),
        ('supermercado', 'Supermercado'),
        ('lazer', 'Lazer'),
        ('educacao', 'Educação'),
        ('eletronicos', 'Eletrônicos'),
        ('saude', 'Saúde'),
        ('casa', 'Casa'),
        ('outros', 'Outros')
    )

    TYPE = (
        ('deposito', 'Depósito'),
        ('pagamento', 'Pagamento'),
        ('transferencia', 'Transferencia'),
        ('compra', 'Compra')
    )

    date = models.DateTimeField(blank=False)
    value = models.DecimalField(max_digits=18, decimal_places=10)
    parcelas = models.PositiveIntegerField()
    categories = models.CharField(max_length=50, choices=CATEGORIES)
    type_transaction = models.CharField(max_length=50, choices=TYPE)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
