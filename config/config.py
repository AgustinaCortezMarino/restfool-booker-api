import os
from pathlib import Path
from dotenv import load_dotenv

# Ruta absoluta al .env desde la raíz del proyecto
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path, override=True)

print("⚠️ DEBUG - USERNAME desde .env:", os.getenv("USERNAME"))
print("⚠️ DEBUG - PASSWORD desde .env:", os.getenv("PASSWORD"))

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("USERNAME", "admin")
PASSWORD = os.getenv("PASSWORD", "password123")
