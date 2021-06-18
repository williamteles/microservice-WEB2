from django.contrib import admin
from .models import Account, Card, Transactions


admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Transactions)
