from django.shortcuts import redirect, render
from .utils import get_account_from_owner, get_card_from_account, get_transactions_from_card, rand_N_digits
import requests
import datetime
from dateutil.relativedelta import relativedelta

MAX_TRIES = 10

def index(request):
    return render(request, 'web/index.html')


def login(request):
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        body = {"username": username, "password": password}

        api_response = requests.post("http://auth-api:8000/auth/login/", json=body)
        payload = api_response.json()

        if api_response.status_code == 200:
            response = redirect("/home")
            response.set_cookie("jwt-access", payload["access"])
            response.set_cookie("jwt-refresh", payload["refresh"])
        # adiciona aqui a chamada pra pegar as informações da conta
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            
            response = render(request, 'register/login.html', dict(context))

        return response

    return render(request, 'register/login.html',{})


def register_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        email = request.POST.get("email")
        body = {"username": username, "password": password, "email": email}

        api_response = requests.post("http://auth-api:8000/auth/user/", json=body)
        payload = api_response.json()

        if api_response.status_code == 201:
            response = redirect("/register/account")
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            response = render(request, 'register/register_user.html', dict(context))

        return response

    return render(request, 'register/register_user.html')


def register_account(request):

    if request.method == "POST":
        type_account = request.POST.get("type_account")
        # owner_id = request.POST.get("owner_id")
        owner_id = 3
        balance = 0
        
        for i in range(MAX_TRIES):
            account_number = str(rand_N_digits(10))

            body = {"owner_id": owner_id, "account_number": account_number,
                    "balance": balance, "type_account": type_account }
            
            api_response = requests.post("http://account-api:8000/acct/account/", json=body)
            payload = api_response.json()

            if api_response.status_code == 201:
                break
            elif i == MAX_TRIES - 1:
                context = {"has_error": True, "error_message": payload["message"]}
                return render(request, 'register/register_account.html', dict(context))
                
        
        account_id = payload["id"]
        prefix_card_number = "3897 2468"
        # password = request.POST.get("card_password")
        password = 2531
        expire_date = str(datetime.date.today() + relativedelta(years=10))
        cvv = str(rand_N_digits(3))
        has_credit = True if type_account == "corrente" else False
        bill = 0
        limit = 1200
        for i in range(MAX_TRIES):
            card_number_part1 = " " + str(rand_N_digits(4))
            card_number_part2 = " " + str(rand_N_digits(4))
            card_number = prefix_card_number + card_number_part1 + card_number_part2

            body = {"card_number": card_number, "expire_date": expire_date,
                    "cvv": cvv, "password": password, "has_credit": has_credit,
                    "bill": bill, "limit": limit, "account": account_id}

            api_response = requests.post("http://account-api:8000/acct/card/", json=body)
            payload = api_response.json()
            if api_response.status_code == 201:
                break
            elif i == MAX_TRIES - 1:
                context = {"has_error": True, "error_message": payload["message"]}
                return render(request, 'register/register_account.html', dict(context))

        return redirect('web:home')

    return render(request,'register/register_account.html',{})


def home(request):
    if request.method == "POST":
        owner_id = request.POST.get("owner_id")
        
        api_response_user = requests.get(f"http://auth-api:8000/auth/user/{owner_id}/")
        payload = api_response_user.json()

        if api_response_user.status_code == 200:
            account = get_account_from_owner(owner_id)
            
            if "has_error" not in account:
                account_card = get_card_from_account(account["id"])

                transactions_account = get_transactions_from_card(account_card["id"])

                context = {"username": payload["username"], "balance": account["balance"], "card": dict(account_card), "transactions": dict(transactions_account)}
                return render(request, "web/home.html", dict(context))
            else:
                context = account
                return render(request, "web/index.html", dict(context))
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            return render(request, "web/inxex.html", dict(context))


    return render(request, "web/home.html", {})
