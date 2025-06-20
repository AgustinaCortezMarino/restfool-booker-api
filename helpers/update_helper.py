import requests
from config import config
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def update_booking(booking_id, token, updated_data):
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.put(url, json=updated_data, headers=headers)
    logging.info(f"🔄 Actualizando reserva ID {booking_id} - Status: {response.status_code}")
    return response

def partial_update_booking(booking_id, token, update_data):
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Cookie": f"token={token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(url, json=update_data, headers=headers)
    logging.info(f"🔧 PATCH /booking/{booking_id} - Status: {response.status_code}")
    return response