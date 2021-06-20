from .models import Account, Card, Transactions
from .serializers import AccountSerializer, CardSerializer, TransactionsSerializer
from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .utils import generate_error_message
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

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
