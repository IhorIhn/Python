import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth

# Налаштування логування: і в консоль, і в файл
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler("test_search.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:5000"

# ---------- Фікстура для аутентифікації ----------
@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    response = session.post(
        auth_url,
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200, f"Auth failed: {response.text}"
    access_token = response.json().get("access_token")
    assert access_token, "Access token not found in response"

    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session

# ---------- Параметри для позитивних тестів ----------
positive_test_data = [
    ("price", 5),
    ("year", 10),
    ("engine_volume", 7),
    ("brand", 3),
    (None, 8),
    ("price", None),
    ("year", 1)
]

@pytest.mark.parametrize("sort_by,limit", positive_test_data)
class TestCarSearchPositive:
    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"[POSITIVE] Running test with params: sort_by={sort_by}, limit={limit}")
        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"Response code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        cars = response.json()
        assert isinstance(cars, list), "Expected list of cars"
        if limit:
            assert len(cars) <= limit, f"Expected max {limit} cars, got {len(cars)}"

# ---------- Негативні кейси ----------
class TestCarSearchNegative:
    def test_no_auth_token(self):
        """Спроба зробити запит без токена авторизації"""
        logger.info("[NEGATIVE] Test: Request without token")
        response = requests.get(f"{BASE_URL}/cars")
        logger.info(f"Response code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        assert response.status_code == 401, f"Expected 401 Unauthorized, got {response.status_code}"

    def test_invalid_sort_field(self, auth_session):
        """Спроба зробити запит із невалідним sort_by"""
        logger.info("[NEGATIVE] Test: Invalid sort_by parameter")
        params = {"sort_by": "non_existing_field", "limit": 5}
        response = auth_session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Response code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        # Flask-код не робить валідацію sort_by → запит поверне 200, але ми перевіряємо, що це не впало
        assert response.status_code == 200, "Expected 200 because server ignores invalid field"
        cars = response.json()
        assert isinstance(cars, list), "Expected list of cars"
        assert len(cars) <= 5, "Limit should still be applied even with invalid sort field"
