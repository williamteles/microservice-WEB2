from typing import ClassVar

from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Account, Card, LoanCredit, AccountType, Transactions, TransactionsType


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['__all__']

class AccountTypeSerializer(ModelSerializer): 
    class Meta:
        model = AccountType
        fields = ['__all__']

class LoanCreditSerializer(ModelSerializer):
    class Meta:
        model = LoanCredit
        fields = ['__all__']

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['__all__']

class TransactionsSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['__all__']

class TransactionsTypeSerializer(ModelSerializer):
    class Meta:
        model = TransactionsType
        fields ['__all__']