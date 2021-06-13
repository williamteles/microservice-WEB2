from .models import User
from .serializers import CustomTokenVerifySerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class LoginView(APIView):

    def post(self, request, *args, **kwargs):

        try:
            username = request.data["username"]
            password = request.data["password"]

            user = User.objects.get(username=username, password=password)

        except KeyError:
            error_message = "Request must contain a username and password"
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            error_message = "Username and Password are invalid, User does not exists"
            return Response({"message": error_message}, status=status.HTTP_404_NOT_FOUND)

        # Set user status as logged
        user.is_active = True
        user.save()

        tokens = self.generate_tokens(user)

        return Response(tokens, status=status.HTTP_200_OK)


    def generate_tokens(self, user):
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        tokens = {"refresh": str(refresh_token), "access": str(access_token)}

        return tokens


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer
