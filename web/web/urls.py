from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'login/', views.login, name='login'),
    path(r'register/user/', views.register_user, name='register_user'),
    path(r'register/account/', views.register_account, name='register_account'),
    path(r'home/', views.home, name='home'),
    path(r'home/payment/<int:account_id>', views.payment, name='payment'),
    path(r'home/deposit/<int:account_id>', views.deposit, name='deposit'),
    path(r'home/transfer/<int:account_id>', views.transfer, name='transfer'),
    path(r'home/buy/<int:account_id>', views.buy, name='buy'),
    path(r'error/', views.error, name='error'),
    path(r'home/changepassword/', views.change_card_password, name='change_password'),
    path(r'home/ajax/extrato', views.extrato, name='extrato'),
 ]
