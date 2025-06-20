import requests
from config import config
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def test_invalid_booking_retrieval():
    non_existent_id = 999999  # Can use any random ID
    url = f"{config.BASE_URL}/booking/{non_existent_id}"
    response = requests.get(url)

    logging.info(f"🚫 Trying to get unexisted booking ID: {non_existent_id}")
    logging.info(f"🔍 Status code: {response.status_code}")
    logging.info(f"🔍 Response: {response.text}")

    assert response.status_code == 404
    logging.info("✅ System response as expected -  404 Not Found")
