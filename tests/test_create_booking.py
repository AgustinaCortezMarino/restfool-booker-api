from helpers.booking_helper import generate_random_booking_data, create_booking
from config import config
import requests


def test_create_booking():
    booking_data = generate_random_booking_data()
    response = create_booking(booking_data)

    assert response.status_code == 200
    booking_response = response.json()

    assert "bookingid" in booking_response
    booking_id = booking_response["bookingid"]

    # Now retrieve the booking and validate it matches
    get_url = f"{config.BASE_URL}/booking/{booking_id}"
    get_response = requests.get(get_url)

    assert get_response.status_code == 200
    retrieved_data = get_response.json()

    # Check some fields (los más importantes)
    assert retrieved_data["firstname"] == booking_data["firstname"]
    assert retrieved_data["lastname"] == booking_data["lastname"]
    assert retrieved_data["totalprice"] == booking_data["totalprice"]
    assert retrieved_data["depositpaid"] == booking_data["depositpaid"]
