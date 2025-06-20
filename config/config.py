import os
from pathlib import Path
from dotenv import load_dotenv

# Root project absolut path
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path, override=True)

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("USERNAME", "admin")
PASSWORD = os.getenv("PASSWORD", "password123")
