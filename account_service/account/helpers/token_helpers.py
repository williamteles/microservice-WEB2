import requests


def extract_token(request):
    token = request.headers.get("Authorization", "")
    return token


def validate_token(token):
    token = token.replace("Bearer ", "")

    response = requests.post("http://auth-api:8000/auth/validate/", json={"token": token})
    json_response = response.json()

    is_valid = True if json_response["code"] == "token_is_valid" else False

    return is_valid, json_response


def get_user_id(response):
    return response["claims"]["user_id"]
