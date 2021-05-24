from .helpers.token_helpers import extract_token, validate_token, get_user_id
from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AccountView(APIView):

    def get(self, request, *args, **kwargs):
        token = extract_token(request)

        if not token:
            error_message = "Authorization Token must not be blank"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        is_valid_token, response = validate_token(token)

        if not is_valid_token:
            error_message = response["detail"]
            return Response({"mesage": error_message}, status=status.HTTP_401_UNAUTHORIZED)

        owner_id = get_user_id(response)

        try:
            account = Account.objects.get(owner_id=owner_id)

        except Account.DoesNotExist:
            error_message = "The User does not have an account"
            return Response({"message": error_message}, status=status.HTTP_404_NOT_FOUND)

        serializer = AccountSerializer(account)

        return Response(serializer.data, status=status.HTTP_200_OK)
