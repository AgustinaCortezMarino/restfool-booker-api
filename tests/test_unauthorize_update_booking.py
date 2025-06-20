from helpers.booking_helper import generate_random_booking_data, create_booking
from helpers.update_helper import update_booking
from config import config
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_unauthorized_update_booking():
    # booking creation
    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Data to update
    updated_data = booking_data.copy()
    updated_data["firstname"] = "Hacker"
    updated_data["lastname"] = "NoToken"

    # Testing update without token (empty token or None)
    # Modify update_booking function to allow optional token
    url = f"{config.BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        # Don't send Cookie with token
    }
    response = requests.put(url, json=updated_data, headers=headers)

    logging.info(f"Updating booking without token, status: {response.status_code}")
    logging.info(f"Response: {response.text}")

    assert response.status_code == 403
    logging.info("✅ System blocked booking update without token")
