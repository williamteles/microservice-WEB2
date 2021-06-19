from random import randint
import requests


def rand_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_account_from_owner(owner_id):
    response = requests.get("http://account-api:8000/acct/account/")
    accounts = response.json()

    if response.status_code == 200:

        for account in accounts:
            if account["owner_id"] == owner_id:
                return account
        return None
    else:
        error = {"has_error": True, "error_message": accounts["message"]}
        return error


def get_card_from_account(account_id):
    response = requests.get("http://account-api:8000/acct/card/").json()
    cards = response.json()

    if response.status_code == 200:
        account_cards = []

        for card in cards:
            if card["account_id"] == account_id:
                account_cards.append(card)
        
        return account_cards
    else:
        error = {"has_error": True, "error_message": cards["message"]}
        return error


def get_transactions_from_card(card):
    response = requests.get("http://account-api:8000/acct/transactions/")
    transactions = response.json()
    
    if response.status_code == 200:
        account_transactions =  []
        
        for transaction in transactions:
            if transaction["card"] == card:
                account_transactions.append(transaction)
        
        return account_transactions
    else:
        error = {"has_error": True, "error_message": transactions["message"]}
        return error
