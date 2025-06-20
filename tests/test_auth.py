import requests
from config import config

def test_valid_authentication():
    url = f"{config.BASE_URL}/auth"
    payload = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    response = requests.post(url, json=payload)
    print("Payload:", payload)
    print("Response status:", response.status_code)
    print("Response body:", response.text)
    print("Auth Response:", response.json())
    assert response.status_code == 200
    assert "token" in response.json(), "Token not found, got: " + str(response.json())


def test_invalid_authentication():
    url = f"{config.BASE_URL}/auth"
    payload = {
        "username": "invalid",
        "password": "wrongpass"
    }
    response = requests.post(url, json=payload)
    print("Invalid Auth Response:", response.json())
    assert response.status_code == 200
    assert response.json().get("reason") == "Bad credentials"