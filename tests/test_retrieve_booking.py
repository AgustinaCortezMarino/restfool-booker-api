from helpers.booking_helper import generate_random_booking_data, create_booking
from config import config
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_retrieve_booking_details():
    # 1. Crear una reserva
    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]
    logging.info(f"🆔 Recuperando reserva con ID: {booking_id}")

    # 2. Obtener los detalles de esa reserva
    get_url = f"{config.BASE_URL}/booking/{booking_id}"
    get_response = requests.get(get_url)
    assert get_response.status_code == 200

    retrieved_data = get_response.json()
    logging.info(f"📦 Datos recuperados: {retrieved_data}")

    # 3. Validar TODOS los campos
    assert retrieved_data["firstname"] == booking_data["firstname"]
    assert retrieved_data["lastname"] == booking_data["lastname"]
    assert retrieved_data["totalprice"] == booking_data["totalprice"]
    assert retrieved_data["depositpaid"] == booking_data["depositpaid"]
    assert retrieved_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert retrieved_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert retrieved_data["additionalneeds"] == booking_data["additionalneeds"]

    logging.info("💚 Validación de todos los campos exitosa")
