from .models import Users
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.tokens import UntypedToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class CustomTokenVerifySerializer(TokenVerifySerializer):
    token = serializers.CharField()

    def validate(self, attrs):
        self.untyped_token = UntypedToken(attrs['token'])
        response = self.format_(self.untyped_token.payload)

        return response

    def format_(self, payload):
        return {
            "code": "token_is_valid",
            "deails": "Token is valid",
            "claims": payload,
        }
