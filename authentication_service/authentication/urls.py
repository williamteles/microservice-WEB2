from django.urls import path
from .views import LoginView, CustomTokenVerifyView, UserList, UserDetail


urlpatterns = [
    path(r"validate/", CustomTokenVerifyView.as_view()),
    path(r"login/", LoginView.as_view()),
    path(r"user/", UserList.as_view()),
    path(r"user/<int:pk>/", UserDetail.as_view())
]
