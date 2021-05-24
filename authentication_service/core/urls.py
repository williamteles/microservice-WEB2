from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r"auth/admin/", admin.site.urls),
    path(r"auth/", include("authentication.urls")),
]
