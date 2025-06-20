import requests
from config import config
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_invalid_booking_retrieval():
    non_existent_id = 999999  # Podés poner cualquier ID alto improbable
    url = f"{config.BASE_URL}/booking/{non_existent_id}"
    response = requests.get(url)

    logging.info(f"🚫 Intentando recuperar reserva inexistente con ID: {non_existent_id}")
    logging.info(f"🔍 Status code recibido: {response.status_code}")
    logging.info(f"🔍 Respuesta: {response.text}")

    assert response.status_code == 404
    logging.info("✅ El sistema respondió correctamente con 404 Not Found")
