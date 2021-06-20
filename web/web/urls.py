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
    path(r'home/payment/<int:account_id>/', views.payment, name='payment'),
    # path(r'deposit/<int:account_id>/', views.deposit, name='deposit'),
    # path('transfer/', views.transfer, name='transfer')
 ]
