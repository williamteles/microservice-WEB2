from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AccountList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, id, format=None):
        account = Account.objects.filter(id_owner = id,)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)
