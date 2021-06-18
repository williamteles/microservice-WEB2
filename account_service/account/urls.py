from django.urls import path
from .views import AccountDetail, AccountTypeReader, AccountList, CardDetail, CardList, TransactionsDetail, TransactionsList, TransactionsTypeReader


urlpatterns = [
    path(r"account/", AccountList.as_view()),
    path(r"account/<int:pk>/", AccountDetail.as_view()),
    path(r"account-type/<int:pk>/", AccountTypeReader.as_view()),
    path(r"card/", CardList.as_view()),
    path(r"card/<int:pk>", CardDetail.as_view()),
    path(r"transactions/", TransactionsList.as_view()),
    path(r"transactions/<int:pk>/", TransactionsDetail.as_view()),
    path(r"transactions-type/<int:pk>/", TransactionsTypeReader.as_view())
]
