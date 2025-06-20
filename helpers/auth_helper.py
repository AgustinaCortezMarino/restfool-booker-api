import requests
from config import config
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def get_auth_token():
    url = f"{config.BASE_URL}/auth"
    payload = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        token = response.json().get("token")
        logging.info(f"🔑 Token obtenido correctamente: {token}")
        return token
    else:
        logging.error(f"❌ Error al obtener token: {response.status_code} - {response.text}")
        return None
