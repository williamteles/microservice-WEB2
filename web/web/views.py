from django.shortcuts import redirect, render
import requests


def index(request):
    return render(request, 'web/index.html')


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        body = {"username": username, "password": password}

        api_response = requests.post("http://localhost:8080/auth/login/", json=body)
        payload = api_response.json()

        if api_response.status_code == 200:
            response = redirect("/home")
            response.set_cookie("jwt-access", payload["access"])
            response.set_cookie("jwt-refresh", payload["refresh"])
        # adiciona aqui a chamada pra pegar as informações da conta
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            response = render(request, 'register/login.html', context)

        return response

    return render(request, 'register/login.html')


def register_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        email = request.POST.get("email")
        body = {"username": username, "password": password, "email": email}

        api_response = requests.post("http://localhost:8080/auth/user/", json=body)
        payload = api_response.json()

        if api_response.status_code == 201:
            response = redirect("/register/account")
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            response = render(request, 'register/register_user.html', context)

        return response

    return render(request, 'register/register_user.html')


def register_account(request):
    return render(request,'register/register_account.html',{})


def home(request):
    return render(request,'web/home.html',{})
