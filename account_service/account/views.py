from django.db.models import query
from .helpers.token_helpers import extract_token, validate_token, get_user_id
from .models import Account, AccountType, Card, Transactions, TransactionsType
from .serializers import AccountSerializer, AccountTypeSerializer, CardSerializer, TransactionsSerializer, TransactionsTypeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

# from account_service.account import serializers


# class AccountView(APIView):

#     def get(self, request, *args, **kwargs):
#         token = extract_token(request)

#         if not token:
#             error_message = "Authorization Token must not be blank"
#             return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

#         is_valid_token, response = validate_token(token)

#         if not is_valid_token:
#             error_message = response["detail"]
#             return Response({"mesage": error_message}, status=status.HTTP_401_UNAUTHORIZED)

#         owner_id = get_user_id(response)

#         try:
#             account = Account.objects.get(owner_id=owner_id)

#         except Account.DoesNotExist:
#             error_message = "The User does not have an account"
#             return Response({"message": error_message}, status=status.HTTP_404_NOT_FOUND)

#         serializer = AccountSerializer(account)

#         return Response(serializer.data, status=status.HTTP_200_OK)


class AccountCRUD(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    
    queryset= Account.objects.all()
    serializer_class = AccountSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar recuperar a conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar criar a conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)            

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar atualizar a conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar deletar a conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class AccountTypeReader(mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset= AccountType.objects.all()
    serializer_class = AccountTypeSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar recuperar o tipo da conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class CardCRUD(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset= Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar recuperar o cartão"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar criar o cartão"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)            

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar atualizar o cartão"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar deletar o cartão"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class TransactionsCRUD(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar recuperar a transação"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar criar a transação"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)            

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar atualizar a transação"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar deletar a transação"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class TransactionsTypeReader(mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset= TransactionsType.objects.all()
    serializer_class = TransactionsTypeSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except:
            error_message = "Erro ao tentar recuperar o tipo da conta"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
