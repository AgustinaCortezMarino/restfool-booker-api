import requests
import logging
from helpers.booking_helper import generate_random_booking_data, create_booking
from config import config

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_unauthorized_delete_booking():
    # Crear reserva
    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Intentar borrar sin token
    url = f"{config.BASE_URL}/booking/{booking_id}"
    response = requests.delete(url)

    logging.info(f"🚫 Intentando eliminar sin token - Status: {response.status_code}")
    logging.info(f"📝 Respuesta: {response.text}")

    # Validamos que NO se pudo eliminar
    assert response.status_code == 403

    # Confirmamos que la reserva aún existe
    get_response = requests.get(url)
    logging.info(f"🔍 Verificando que la reserva aún exista - Status: {get_response.status_code}")
    assert get_response.status_code == 200

    logging.info("✅ El sistema protegió la reserva contra eliminación sin token")
