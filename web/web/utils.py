from random import randint
from datetime import datetime
import requests


def rand_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_account_from_owner(owner_id):
    response = requests.get("http://account-api:8000/acct/account/")
    accounts = response.json()

    if response.status_code == 200:
        if len(accounts) == 0:
            return accounts

        for account in accounts:
            if account["owner_id"] == owner_id:
                return account
    else:
        error = {"has_error": True, "error_message": accounts["message"]}
        return error


def get_card_from_account(account_id):
    response = requests.get("http://account-api:8000/acct/card/")
    cards = response.json()

    if response.status_code == 200:
        if len(cards) == 0:
            return cards
        
        for card in cards:
            if card["account"] == account_id:
                expire_date_obj = datetime.strptime(card["expire_date"], '%Y-%m-%d')
                expire_date = datetime.strftime(expire_date_obj, '%m/%Y')
                card["expire_date"] = expire_date

                return card        
    else:
        error = {"has_error": True, "error_message": cards["message"]}
        return error


def get_transactions_from_account(account_id):
    response = requests.get("http://account-api:8000/acct/transactions/")
    transactions = response.json()
    
    if response.status_code == 200:
        account_transactions =  []
        
        for transaction in transactions:
            if transaction["account"] == account_id:
                date_obj = datetime.strptime(transaction["date"], '%Y-%m-%d')
                date = datetime.strftime(date_obj, '%d/%m/%Y')
                transaction["date"] = date
                account_transactions.append(transaction)
        
        return account_transactions
    else:
        error = {"has_error": True, "error_message": transactions["message"]}
        return error

def create_transaction(body):
    api_response = requests.post(f"http://account-api:8000/acct/transactions/", json=body)
    payload = api_response.json()

    if api_response.status_code is not 201:
        error = {"has_error": True, "error_message": payload["message"]}
        return error
    else:
        return "Created"
