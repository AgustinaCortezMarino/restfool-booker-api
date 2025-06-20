# 🧪 RESTful Booker API Test Suite
This project contains a fully automated test suite for the public [Restful Booker API](https://restful-booker.herokuapp.com/).  
It was developed as part of a technical challenge to showcase clean code practices, modularity, reusability, and effective validation.
---
## 🚀 Tech Stack
- 🐍 Python 3
- ✅ Pytest
- 🔥 Faker (randomized data generation)
- 📡 Requests
- 💻 PyCharm (recommended IDE)
---
## 📁 Project Structure
    restful-booker-api/
    ├── config/
    │ └── config.py # Base URL, credentials, etc.
    ├── helpers/
    │ ├── auth_helper.py # Handles token authentication
    │ ├── booking_helper.py # Data generation and creation helpers
    │ └── update_helper.py # Functions for update requests
    ├── tests/
    │ ├── test_auth.py # TC 1.1 / 1.2 - Valid & Invalid auth
    │ ├── test_create_booking.py # TC 2.1 - Create booking
    │ ├── test_retrieve_booking.py # TC 2.2 / 2.3 - Valid & invalid GET
    │ ├── test_update_booking.py # TC 3.1 - PUT with token
    │ ├── test_unauthorized_update.py # TC 3.2 - PUT without token
    │ ├── test_delete_booking.py # TC 4.1 - DELETE with token
    │ ├── test_unauthorized_delete.py # TC 4.2 - DELETE without token
    │ └── test_partial_update.py # TC 5.1 - PATCH single field
    ├── requirements.txt
    └── README.md
---
## ⚙️ Setup

### 1. Clone the repository:
- git clone https://github.com/AgustinaCortezMarino/restfool-booker-api
- cd restful-booker-api

### 2. Create and activate a virtual environment:
- python -m venv .venv
- .venv\Scripts\activate   # Windows

### 3. Install dependencies:
- pip install -r requirements.txt

### 4. Configuration file: update config/config.py if needed:
- BASE_URL = https://restful-booker.herokuapp.com
- USERNAME = admin
- PASSWORD = password123

---
## ▶️ Run the Tests
#### Basic test run:
- pytest -v

## 🙋‍♀️ Author
### Agustina Cortez Marino