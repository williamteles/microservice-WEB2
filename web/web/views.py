from django.shortcuts import redirect, render
from .utils import create_account, create_card, create_transaction, delete_account, get_account_by_account_number, get_account_by_id, get_account_from_owner, get_card_from_account, get_transactions_from_account, rand_N_digits, update_account_balance, update_card_bill
import requests
from datetime import datetime, date
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
            request.session["jwt-access"] = payload["tokens"]["access"]
            request.session["jwt-refresh"] = payload["tokens"]["refresh"]
            request.session["user_id"] = payload["user_id"]
            response = redirect("/home")
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
            request.session["user_id"] = payload["id"]
            response = redirect("/register/account")
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            response = render(request, 'register/register_user.html', dict(context))

        return response

    return render(request, 'register/register_user.html')


def register_account(request):

    if request.method == "POST":
        type_account = request.POST.get("type_account")
        owner_id = request.session["user_id"]
        balance = 0
        
        for i in range(MAX_TRIES):
            account_number = str(rand_N_digits(10))
            body = {
                "owner_id": owner_id,
                "account_number": account_number,
                "balance": balance,
                "type_account": type_account
                }
            
            account = create_account(body)

            if "has_error" not in account:
                account_id = account["id"]
                prefix_card_number = "3897 2468"
                password = request.POST.get("card_password")
                expire_date = str(date.today() + relativedelta(years=10))
                cvv = str(rand_N_digits(3))
                has_credit = True if type_account == "corrente" else False
                bill = 0
                limit = 1200

                for i in range(MAX_TRIES):
                    card_number_part1 = " " + str(rand_N_digits(4))
                    card_number_part2 = " " + str(rand_N_digits(4))
                    card_number = prefix_card_number + card_number_part1 + card_number_part2
                    body = {
                        "card_number": card_number,
                        "expire_date": expire_date,
                        "cvv": cvv,
                        "password": password,
                        "has_credit": has_credit,
                        "bill": bill,
                        "limit": limit,
                        "account": account_id
                        }
                    
                    card = create_card(body)

                    if "has_error" not in card:
                        return redirect('web:login')

                    elif i == MAX_TRIES - 1:
                        response_delete_account = delete_account(account_id)
                        response_delete_account["error_message"] = "Não foi possível criar a conta"
                        return render(request, 'register/register_account.html', dict(response_delete_account))
                        
                    else:
                        continue

            elif i == MAX_TRIES - 1:
                context = {"has_error": True, "error_message": "Não foi possível criar a conta"}
                return render(request, 'register/register_account.html', dict(context))

            else:
                continue
                
    return render(request,'register/register_account.html',{})


def home(request):
    if request.method == "GET":
        owner_id = request.session["user_id"]
        
        api_response_user = requests.get(f"http://auth-api:8000/auth/user/{owner_id}/")
        payload = api_response_user.json()

        if api_response_user.status_code == 200:
            account = get_account_from_owner(owner_id)
            
            if "has_error" not in account:
                account_card = get_card_from_account(account["id"])

                transactions_account = get_transactions_from_account(account["id"])

                context = {"username": payload["username"], "account": account, "card": account_card, "transactions": list(reversed(transactions_account))}
                return render(request, 'web/home.html', dict(context))
            else:
                context = account
                return render(request, "error/erro.html", dict(context))
        else:
            context = {"has_error": True, "error_message": payload["message"]}
            return render(request, "error/erro.html", dict(context))

    return render(request, "web/home.html")


def payment(request, account_id):

    if request.method == "POST":

        date_transaction = datetime.strftime(date.today(), '%Y-%m-%d')
        time_transaction = datetime.strftime(datetime.now(), "%H:%M:%S")
        payment_value = float(request.POST.get("payment_value"))
        type_transaction = "Pagamento"

        transaction_body = {
            "date": date_transaction,
            "time": time_transaction,
            "value": payment_value,
            "type_transaction": type_transaction,
            "account": account_id
            }
        
        account = get_account_by_id(account_id)

        if "has_error" not in account:
            balance = float(account["balance"])
            final_balance = balance - payment_value

            if final_balance < 0:
                context = {"has_error": True, "error_message": "Saldo Insuficiente"}
                return render(request, 'error/erro.html', dict(context))
            else:
                card = get_card_from_account(account_id)
                final_bill = float(card["bill"])- payment_value
                    
                if final_bill < 0:
                    final_balance += abs(final_bill)

                    bill_update = update_card_bill(card["id"], 0)
                    
                    if "has_error" in bill_update:
                        return render(request, 'error/erro.html', dict(bill_update))

                else:
                    bill_update = update_card_bill(card["id"], final_bill)

                    if "has_error" in bill_update:
                        return render(request, 'error/erro.html', dict(bill_update))

                balance_update = update_account_balance(account_id, final_balance)
                        
                if "has_error" not in balance_update:
                    response_transaction = create_transaction(transaction_body)

                    if "has_error" not in response_transaction:
                        return redirect('web:home')
                    else:
                        return render(request, 'error/erro.html', dict(response_transaction))
                else:
                    return render(request, 'error/erro.html', dict(balance_update))
        
        else:
            return render(request, 'error/erro.html', dict(account))

    return render(request, "web/home.html")


def deposit(request, account_id):
    
    if request.method == "POST":
        date_transaction = datetime.strftime(date.today(), '%Y-%m-%d')
        time_transaction = datetime.strftime(datetime.now(), "%H:%M:%S")
        deposit_value = float(request.POST.get("deposit_value"))
        type_transaction = "Depósito"

        transaction_body = {
            "date": date_transaction,
            "time": time_transaction,
            "value": deposit_value,
            "type_transaction": type_transaction,
            "account": account_id
            }

        account = get_account_by_id(account_id)

        if "has_error" not in account:
            balance = float(account["balance"])
            final_balance = balance + deposit_value

            update_balance = update_account_balance(account_id, final_balance)

            if "has_error" not in update_balance:
                response_transaction = create_transaction(transaction_body)

                if "has_error" not in response_transaction:
                    return redirect('web:home')
                
                else:
                    return render(request, 'error/erro.html', dict(response_transaction))
        
        else:
            return render(request, 'web/home.html', dict(account))
    
    return render(request, "web/home.html")


def transfer(request, account_id):

    if request.method == "POST":

        date_transaction = datetime.strftime(date.today(), '%Y-%m-%d')
        time_transaction = datetime.strftime(datetime.now(), "%H:%M:%S")
        transfer_value = float(request.POST.get("transfer_value"))
        account_transfer_number = request.POST.get("account_transfer_number")
        type_transaction = "Transferência"

        account = get_account_by_id(account_id)

        account_transfer = get_account_by_account_number(account_transfer_number)

        if ("has_error" not in account) and ("has_error" not in account_transfer):
            transaction_body = {
                "date": date_transaction,
                "time": time_transaction,
                "value": transfer_value,
                "type_transaction": type_transaction,
                "transfer_account": account_transfer["id"],
                "account": account_id
                }

            balance = float(account["balance"])
            final_balance = balance - transfer_value

            if final_balance < 0:
                context = {"has_error": True, "error_message": "Saldo Insuficiente"}
                return render(request, 'error/erro.html', dict(context))
            
            else:
                balance_transfer =  float(account_transfer["balance"])
                final_balance_transfer = balance_transfer + transfer_value
                
                update_balance = update_account_balance(account_id, final_balance)
                if "has_error" not in update_balance:
                    update_transfer_account_balance = update_account_balance(account_transfer["id"], final_balance_transfer)
                
                    if "has_error" not in update_transfer_account_balance:
                        response_transaction = create_transaction(transaction_body)

                        if "has_error" not in response_transaction:
                            return redirect('web:home')
    
                        else:
                            return render(request, 'error/erro.html', dict(response_transaction))
                    
                    else:
                        return render(request, 'error/erro.html', dict(update_transfer_account_balance))
                
                else:
                    return render(request, 'error/erro.html', dict(update_balance))

        elif "has_error" not in account:
            return render(request, 'error/erro.html', dict(account_transfer))
        else:
            return render(request, 'error/erro.html', dict(account))
    
    return render(request, "web/home.html")


def buy(request, account_id):
    
    if request.method == "POST":
        payment_type = request.POST.get("payment_type")
        buy_value = float(request.POST.get("buy_value"))
        categories = request.POST.get("buy_type")
        date_transaction = datetime.strftime(date.today(), '%Y-%m-%d')
        time_transaction = datetime.strftime(datetime.now(), "%H:%M:%S")
        type_transaction = "Compra"

        account = get_account_by_id(account_id)

        if "has_error" not in account:
            
            if payment_type == "Débito":
                transaction_body = {
                        "date": date_transaction,
                        "time": time_transaction,
                        "value": buy_value,
                        "categories": categories,
                        "type_transaction": type_transaction,
                        "payment_type": payment_type,
                        "account": account_id
                        }
                
                balance = float(account["balance"])
                final_balance = balance - buy_value

                if final_balance < 0:
                    context = {"has_error": True, "error_message": "Saldo Insuficiente"}
                    return render(request, 'error/erro.html', dict(context))
                
                else:
                    update_response = update_account_balance(account_id, final_balance)

                    if "has_error" not in update_response:
                        response_transaction = create_transaction(transaction_body)

                        if "has_error" not in response_transaction:
                            return redirect('web:home')
                        else:
                            return render(request, 'error/erro.html', dict(response_transaction))
                    
                    else:
                        return render(request, 'error/erro.html', dict(update_response))
            
            elif payment_type == "Crédito":
                card = get_card_from_account(account_id)

                if "has_error" not in card:

                    transaction_body = {
                            "date": date_transaction,
                            "time": time_transaction,
                            "value": buy_value,
                            "categories": categories,
                            "type_transaction": type_transaction,
                            "payment_type": payment_type,
                            "account": account_id,
                            "card": card["id"]
                            }
                    
                    bill = float(card["bill"])
                    final_bill = bill + buy_value

                    if final_bill > float(card["limit"]):
                        context = {"has_error": True, "error_message": "Limite Insuficiente"}
                        return render(request, 'error/erro.html', dict(context))
                    
                    else:
                        update_response = update_card_bill(card["id"], final_bill)

                        if "has_error" not in update_response:
                            response_transaction = create_transaction(transaction_body)

                            if "has_error" not in response_transaction:
                                return redirect('web:home')
                            else:
                                return render(request, 'error/erro.html', dict(response_transaction))
                        
                        else:
                            return render(request, 'error/erro.html', dict(update_response))

                else:
                    return render(request, 'error/erro.html', dict(card))

            else:
                context = {"has_error": True, "error_message": "Opção de pagamento inválida"}
                return render(request, 'error/erro.html', dict(context))

    return render(request, "web/home.html") 


def error(request):
    return render(request, 'error/erro.html')
