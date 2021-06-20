from rest_framework.serializers import ModelSerializer
from .models import Account, Card, Transactions


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class TransactionsSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
