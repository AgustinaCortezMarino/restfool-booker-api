import requests
import logging
from helpers.booking_helper import generate_random_booking_data, create_booking
from helpers.auth_helper import get_auth_token
from helpers.delete_helper import delete_booking
from config import config

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_delete_booking():
    # Crear reserva
    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Obtener token
    token = get_auth_token()
    assert token is not None

    # Eliminar reserva
    delete_response = delete_booking(booking_id, token)
    assert delete_response.status_code in [201, 204]

    # Confirmar que fue eliminada (esperamos 404)
    get_url = f"{config.BASE_URL}/booking/{booking_id}"
    get_response = requests.get(get_url)
    logging.info(f"🔍 Verificando que la reserva fue eliminada. Status: {get_response.status_code}")
    assert get_response.status_code == 404

    logging.info("✅ Reserva eliminada correctamente y confirmada su inexistencia")
