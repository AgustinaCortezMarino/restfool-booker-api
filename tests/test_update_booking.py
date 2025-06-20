from helpers.booking_helper import generate_random_booking_data, create_booking
from helpers.auth_helper import get_auth_token
from helpers.update_helper import update_booking
from config import config
import requests
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_update_booking():

    booking_data = generate_random_booking_data()
    create_response = create_booking(booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Get token
    token = get_auth_token()
    assert token is not None

    # Updated data
    updated_data = booking_data.copy()
    updated_data["firstname"] = "UpdatedName"
    updated_data["lastname"] = "UpdatedLastName"

    #  update
    update_response = update_booking(booking_id, token, updated_data)
    assert update_response.status_code == 200

    # Validate update
    get_url = f"{config.BASE_URL}/booking/{booking_id}"
    get_response = requests.get(get_url)
    assert get_response.status_code == 200

    retrieved_data = get_response.json()
    logging.info(f"📦 Data after update: {retrieved_data}")

    assert retrieved_data["firstname"] == updated_data["firstname"]
    assert retrieved_data["lastname"] == updated_data["lastname"]
    assert retrieved_data["totalprice"] == updated_data["totalprice"]
    assert retrieved_data["depositpaid"] == updated_data["depositpaid"]
    assert retrieved_data["bookingdates"]["checkin"] == updated_data["bookingdates"]["checkin"]
    assert retrieved_data["bookingdates"]["checkout"] == updated_data["bookingdates"]["checkout"]
    assert retrieved_data["additionalneeds"] == updated_data["additionalneeds"]

    logging.info("💚 Update and validation passed")
