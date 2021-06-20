from django.urls import path
from .views import AccountDetail, AccountList, CardDetail, CardList, TransactionsDetail, TransactionsList


urlpatterns = [
    path(r"account/", AccountList.as_view()),
    path(r"account/<int:pk>/", AccountDetail.as_view()),
    path(r"card/", CardList.as_view()),
    path(r"card/<int:pk>", CardDetail.as_view()),
    path(r"transactions/", TransactionsList.as_view()),
    path(r"transactions/<int:pk>/", TransactionsDetail.as_view())
]
