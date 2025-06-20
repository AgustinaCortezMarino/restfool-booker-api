import requests
from config import config
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def delete_booking(booking_id, token):
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Cookie": f"token={token}"
    }
    response = requests.delete(url, headers=headers)
    logging.info(f"🗑️ Eliminando reserva {booking_id} - Status: {response.status_code}")
    return response
