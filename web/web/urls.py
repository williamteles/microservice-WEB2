from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/user/',views.register_user,name='register_user'),
]