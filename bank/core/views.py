from django.http.response import HttpResponse
from django.shortcuts import render
from core.models import Account

# Create your views here.

def index(request):
    bank = Account.objects.all()

    for account in bank:
        print(account.number_account)
        
    return HttpResponse('hello world')