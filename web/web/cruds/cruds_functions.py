from datetime import datetime
import requests


################################################################################################################################
######################################################## ACCOUNT ###############################################################
################################################################################################################################

def create_account(body):
    api_response = requests.post(f"http://account-api:8000/acct/account/", json=body)
    payload = api_response.json()

    if api_response.status_code != 201:
        error = {"has_error": True, "error_message": payload["message"]}
        return error
    
    return payload


def get_account_from_owner(owner_id):
    response = requests.get("http://account-api:8000/acct/account/")
    accounts = response.json()

    if response.status_code == 200:
        if len(accounts) == 0:
            return {}

        for account in accounts:
            if account["owner_id"] == owner_id:
                return account
    else:
        error = {"has_error": True, "error_message": accounts["message"]}
        return error


def get_account_by_id(account_id):
    api_response = requests.get(f"http://account-api:8000/acct/account/{account_id}")
    account = api_response.json()

    if api_response.status_code == 200:
        return account
    
    else:
        error = {"has_error": True, "error_message": account["message"]}
        return error


def get_account_by_account_number(account_number):
    api_response = requests.get("http://account-api:8000/acct/account/")
    accounts = api_response.json()
    
    if api_response.status_code == 200:
        for account in accounts:
            
            if account["account_number"] == account_number:
                
                return account
        
        error = {"has_error": True, "error_message": "Conta não encontrada"}
        return error
    
    else:
        error = {"has_error": True, "error_message": payload["message"]}
        return error


def update_account_balance(acocunt_id, final_balance):
    body = {"id": acocunt_id, "balance": final_balance}
    api_response = requests.put(f"http://account-api:8000/acct/accountbalance/{acocunt_id}", json=body)

    if api_response.status_code not in (200, 204):
        error = {"has_error": True, "error_message": "Atualização de saldo não sucedida"}
        return error
    
    return {}


def delete_account(account_id):
    api_response = requests.delete(f"http://account-api:8000/acct/account/{account_id}")
    payload = api_response.json()

    if api_response.status_code not in (200, 204):
        error = {"has_error": True, "error_message": ""}
        return error
    
    return payload

################################################################################################################################
######################################################### CARD #################################################################
################################################################################################################################

def create_card(body):
    api_response = requests.post(f"http://account-api:8000/acct/card/", json=body)
    payload = api_response.json()

    if api_response.status_code != 201:
        error = {"has_error": True, "error_message": payload["message"]}
        return error
    
    return payload


def get_card_from_account(account_id, convert=True):
    response = requests.get("http://account-api:8000/acct/card/")
    cards = response.json()

    if response.status_code == 200:
        if len(cards) == 0:
            return cards
        
        for card in cards:
            if card["account"] == account_id:
                if convert:
                    expire_date_obj = datetime.strptime(card["expire_date"], '%Y-%m-%d')
                    expire_date = datetime.strftime(expire_date_obj, '%m/%Y')
                    card["expire_date"] = expire_date

                return card        
    else:
        error = {"has_error": True, "error_message": cards["message"]}
        return error


def update_card(card):
    card_id = card["id"]
    api_response = requests.put(f"http://account-api:8000/acct/card/{card_id}", json=card)
    payload = api_response.json()
    
    if api_response.status_code not in (200, 204):
        error = {"has_error": True, "error_message": "Atualização de cartão não sucedida"}
        return error
    
    return payload


def update_card_bill(card_id, final_bill):
    body = {"id": card_id, "bill": final_bill}
    api_response = requests.put(f"http://account-api:8000/acct/cardbill/{card_id}", json=body)
    payload = api_response.json()

    if api_response.status_code not in (200, 204):
        error = {"has_error": True, "error_message": "Atualização de fatura não sucedida"}
        return error
    
    return payload


def delete_card(card_id):
    api_response = requests.delete(f"http://account-api:8000/acct/card/{card_id}")
    payload = api_response.json()

    if api_response.status_code not in (200, 204):
        error = {"has_error": True, "error_message": ""}
        return error
    
    return payload

################################################################################################################################
##################################################### TRANSACTION ##############################################################
################################################################################################################################

def create_transaction(body):
    api_response = requests.post(f"http://account-api:8000/acct/transactions/", json=body)
    payload = api_response.json()

    if api_response.status_code != 201:
        error = {"has_error": True, "error_message": payload["message"]}
        return error

    return payload


def get_transactions_from_account(account_id):
    response = requests.get("http://account-api:8000/acct/transactions/")
    transactions = response.json()
    
    if response.status_code == 200:
        account_transactions =  []
        
        for transaction in transactions:
            date_converted = False

            if transaction["account"] == account_id:
                date_obj = datetime.strptime(transaction["date"], '%Y-%m-%d')
                date = datetime.strftime(date_obj, '%d/%m/%Y')
                transaction["date"] = date
                date_converted = True

                account_transactions.append(transaction)

            account = get_account_by_id(account_id)

            if transaction["transfer_account"] == account["account_number"]:
                if not date_converted:
                    date_obj = datetime.strptime(transaction["date"], '%Y-%m-%d')
                    date = datetime.strftime(date_obj, '%d/%m/%Y')
                    transaction["date"] = date

                transaction["type_transaction"] = "Recebido"

                account_transactions.append(transaction)
        
        return account_transactions
    else:
        error = {"has_error": True, "error_message": transactions["message"]}
        return error


def get_transaction_by_id(transaction_id, account_id):
    api_response = requests.get(f"http://account-api:8000/acct/transactions/{transaction_id}")
    transaction = api_response.json()

    if api_response.status_code == 200:
        date_obj = datetime.strptime(transaction["date"], '%Y-%m-%d')
        date = datetime.strftime(date_obj, '%d/%m/%Y')
        transaction["date"] = date

        account = get_account_by_id(account_id)

        if transaction["transfer_account"] == account["account_number"]:
            transaction["type_transaction"] = "Recebido"
            
            sender_account_id = transaction["account"]
            sender_account = get_account_by_id(sender_account_id)

            if "has_error" not in sender_account:
                transaction["account"] = sender_account["account_number"]
            else:
                transaction["account"] = " "

        if transaction["card"] is not None:
            card_id = transaction["card"]
            card = requests.get(f"http://account-api:8000/acct/card/{card_id}").json()
            transaction["card"] = card["card_number"]
        
        return transaction
    
    else:
        error = {"has_error": True, "error_message": transaction["message"]}
        return error


def delete_transactions(account_id):
    api_response = requests.get(f"http://account-api:8000/acct/transactions/")
    trasactions = api_response.json()
    
    if api_response.status_code == 200:
        
        for transaction in trasactions:
            
            if transaction["account"] == account_id:
                id = transaction["id"]
                api_response = requests.delete(f"http://account-api:8000/acct/transactions/{id}")
            
        return {}        
    
    else:
        error = {"has_error": True, "error_message": trasactions["message"]}
        return error

################################################################################################################################
########################################################## USER ################################################################
################################################################################################################################

def create_user(body):
    api_response = requests.post(f"http://auth-api:8000/auth/user/", json=body)
    payload = api_response.json()

    if api_response.status_code != 201:
        error = {"has_error": True, "error_message": payload["message"]}
        return error

    return payload


def get_user_by_id(user_id):
    api_response = requests.get(f"http://auth-api:8000/auth/user/{user_id}")
    user = api_response.json()

    if api_response.status_code == 200:
        return user
    
    else:
        error = {"has_error": True, "error_message": user["message"]}
        return error