from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/user/',views.register_user,name='register_user'),
    path('register/account/',views.register_account,name='register_account'),
    path('home',views.home,name='home'),
    path('payment/<int:card_id>',views.payment,name='payment'),
    path('deposit/<int:account_id>',views.deposit,name='deposit'),
]
