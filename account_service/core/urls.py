from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r"acct/admin/", admin.site.urls),
    path(r"acct/", include("account.urls"))
]
