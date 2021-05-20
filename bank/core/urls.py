from django.urls import path
from core import views

urlpatterns = [
    path('account/<int:id>/', views.AccountList.as_view()),
]