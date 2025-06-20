from helpers.booking_helper import generate_random_booking_data, create_booking
from helpers.update_helper import update_booking
from config import config
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_unauthorized_update_booking():
    # Crear reserva inicial
    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Datos para actualizar
    updated_data = booking_data.copy()
    updated_data["firstname"] = "Hacker"
    updated_data["lastname"] = "NoToken"

    # Intentar update sin token (pasamos token vacío o None)
    # Modificamos la función update_booking para permitir token opcional
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        # No enviamos Cookie con token
    }
    response = requests.put(url, json=updated_data, headers=headers)

    logging.info(f"Intentando actualizar reserva sin token, status: {response.status_code}")
    logging.info(f"Respuesta: {response.text}")

    assert response.status_code == 403
    logging.info("✅ El sistema bloqueó la actualización sin token correctamente")
