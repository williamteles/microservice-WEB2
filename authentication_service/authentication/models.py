from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_superuser = None
    first_name = None
    is_staff = None
    last_login = None
    last_name = None
    date_joined = None
    email = None

# from django.contrib.auth.hashers import make_password

# x = User(1, make_password("1234"), "jonas", False)
# x.save()

