import pytest
from selenium import webdriver
from tracking_page import NovaPoshtaTrackingPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tracking_status(driver):
    tracking_number = "20450383333333"  # підстав свій реальний номер
    expected_status = "Посилка отримана"

    tracking_page = NovaPoshtaTrackingPage(driver)
    tracking_page.open()
    tracking_page.enter_tracking_number(tracking_number)
    status = tracking_page.get_parcel_status()

    assert status == expected_status, f"Очікував: {expected_status}, але отримав: {status}"
