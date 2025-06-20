import requests
from faker import Faker
from config import config
import logging

fake = Faker()

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def generate_random_booking_data():
    booking = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=1000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date_this_year().isoformat(),
            "checkout": fake.date_this_year().isoformat(),
        },
        "additionalneeds": fake.word()
    }
    logging.info(f"🔧 Booking generado aleatoriamente: {booking}")
    return booking

def create_booking(booking_data):
    url = f"{config.BASE_URL}/booking"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=booking_data, headers=headers)

    if response.status_code == 200 and "bookingid" in response.json():
        logging.info(f"✅ Reserva creada con éxito. ID: {response.json()['bookingid']}")
    else:
        logging.warning(f"❌ Error al crear reserva: {response.status_code} - {response.text}")

    return response
