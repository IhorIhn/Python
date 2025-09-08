import pytest
import allure
from selenium import webdriver
from tracking_page import NovaPoshtaTrackingPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Трекінг посилок Нова Пошта")
@allure.story("Перевірка статусу посилки за номером")
@allure.title("Перевірка статусу посилки Нова Пошта")
@allure.description("Тест перевіряє, чи статус посилки збігається з очікуваним")
def test_tracking_status(driver):
    tracking_number = "20400471342310"
    expected_status = "Отримана"

    with allure.step("Відкрити сторінку трекінгу"):
        tracking_page = NovaPoshtaTrackingPage(driver)
        tracking_page.open()

    with allure.step(f"Ввести номер {tracking_number}"):
        tracking_page.enter_tracking_number(tracking_number)

    with allure.step("Отримати статус посилки"):
        status = tracking_page.get_parcel_status()
        allure.attach(status, name="Отриманий статус", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Перевірити статус"):
        assert status == expected_status, f"Очікував: {expected_status}, але отримав: {status}"
