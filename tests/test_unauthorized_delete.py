import requests
import logging
from helpers.booking_helper import generate_random_booking_data, create_booking
from config import config

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_unauthorized_delete_booking():

    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Trying to delete without token
    url = f"{config.BASE_URL}/booking/{booking_id}"
    response = requests.delete(url)

    logging.info(f"🚫 Trying to delete without token - Status: {response.status_code}")
    logging.info(f"📝 Response: {response.text}")

    # Validate delete not possible
    assert response.status_code == 403

    # Confirm booking still existing
    get_response = requests.get(url)
    logging.info(f"🔍 Verifying booking - Status: {get_response.status_code}")
    assert get_response.status_code == 200

    logging.info("✅ System protect booking elimination without token")
