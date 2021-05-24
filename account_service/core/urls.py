from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path(r'account/admin/', admin.site.urls),
    path(r'account/', include('account.urls'))
]
