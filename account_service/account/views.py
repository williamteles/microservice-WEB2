from .models import Account, Card, Transactions
from .serializers import AccountSerializer, AccountUpdateBalanceSerializer, CardSerializer, CardUpdateBillSerializer, TransactionsSerializer
from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .utils import generate_error_message
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class AccountDetail(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            response = self.retrieve(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

        return response

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response

    def delete(self, request, *args, **kwargs):
        try:
            response = self.destroy(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class AccountList(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            response = self.create(request, *args, **kwargs)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class CardDetail(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset= Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        try:
            response = self.retrieve(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

        return response

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response

    def delete(self, request, *args, **kwargs):
        try:
            response = self.destroy(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class CardList(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            response = self.create(request, *args, **kwargs)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class TransactionsDetail(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get(self, request, *args, **kwargs):
        try:
            response = self.retrieve(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

        return response

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response

    def delete(self, request, *args, **kwargs):
        try:
            response = self.destroy(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class TransactionsList(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            response = self.create(request, *args, **kwargs)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response


class CardUpdateBill(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Card.objects.all()
    serializer_class = CardUpdateBillSerializer

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response

class AccountUpdateBalance(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountUpdateBalanceSerializer

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
        except Http404 as e:
            response = Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            error_message = generate_error_message(e.detail)
            response = Response({"message": error_message}, status=e.status_code)

        return response
