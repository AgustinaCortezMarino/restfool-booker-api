import requests
import logging
from faker import Faker
from helpers.booking_helper import generate_random_booking_data, create_booking
from helpers.auth_helper import get_auth_token
from helpers.update_helper import partial_update_booking
from config import config

fake = Faker()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_partial_update_booking():
    # Crear reserva original
    original_data = generate_random_booking_data()
    create_response = create_booking(original_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Obtener token válido
    token = get_auth_token()
    assert token is not None

    # Generar nuevo nombre para actualizar
    new_firstname = fake.first_name()
    update_data = {
        "firstname": new_firstname
    }

    # Ejecutar PATCH
    patch_response = partial_update_booking(booking_id, token, update_data)
    assert patch_response.status_code == 200

    response_data = patch_response.json()
    logging.info(f"👑 PATCH Response Data: {response_data}")

    # Validar que solo firstname cambió, y el resto se mantuvo
    assert response_data["firstname"] == new_firstname
    assert response_data["lastname"] == original_data["lastname"]
    assert response_data["totalprice"] == original_data["totalprice"]
    assert response_data["depositpaid"] == original_data["depositpaid"]
    assert response_data["bookingdates"]["checkin"] == original_data["bookingdates"]["checkin"]
    assert response_data["bookingdates"]["checkout"] == original_data["bookingdates"]["checkout"]
    assert response_data["additionalneeds"] == original_data["additionalneeds"]

    logging.info("✅ PATCH exitoso: solo firstname fue actualizado correctamente")
