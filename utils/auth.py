import requests
from config import config

def get_token():
    url = f"{config.BASE_URL}/auth"
    payload = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json().get("token")
