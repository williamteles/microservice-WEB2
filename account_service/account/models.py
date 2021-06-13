from django.db import models


class AccountType(models.Model):
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
    owner_id = models.IntegerField(unique=True)
    type_account = models.ForeignKey(AccountType, on_delete=models.PROTECT)


class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expire_date = models.DateField(blank=False)
    cvv = models.CharField(max_length=3)
    password = models.PositiveIntegerField(max_length=4, blank=False, null=False)
    has_debit = models.BooleanField(default=False)
    has_credit = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    bill = models.DecimalField(max_digits=18, decimal_places=10)
    limit = models.DecimalField(max_digits=18, decimal_places=10)
    account = models.Model(Account, on_delete=models.PROTECT)


class TransactionsType(models.Model):
    TYPE = (
        ('deposito', 'Depósito'),
        ('pagamento', 'Pagamento'),
        ('transferencia', 'Transferencia'),
        ('compra', 'Compra')
    )

    type = models.CharField(max_length=50, choices=TYPE, null=False)

    def __str__(self):
        return f"{self.type}"
    
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

    date = models.DateTimeField(blank=False)
    value = models.DecimalField(max_digits=18, decimal_places=10)
    parcelas = models.PositiveIntegerField(max_length=3)
    categories = models.CharField(max_length=50, choices=CATEGORIES)
    type_transaction = models.ForeignKey(TransactionsType, on_delete=models.PROTECT)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
