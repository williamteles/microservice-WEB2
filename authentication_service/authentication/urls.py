from django.urls import path
from .views import LoginView, CustomTokenVerifyView


urlpatterns = [
    path(r"validate/", CustomTokenVerifyView.as_view()),
    path(r"login/", LoginView.as_view())
]
