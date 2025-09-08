import time
import random
import string
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


def generate_random_email():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"


def test_user_registration(driver, click_element, fill_input, wait):
    # Крок 1: Натиснути на кнопку "Sign up"
    click_element(LoginPage.REGISTER_BTN)

    # Крок 2: Заповнюємо форму реєстрації
    fill_input(RegistrationPage.NAME_INPUT, "Test")
    fill_input(RegistrationPage.LASTNAME_INPUT, "User")
    email = generate_random_email()
    fill_input(RegistrationPage.EMAIL_INPUT, email)
    fill_input(RegistrationPage.PASSWORD_INPUT, "Test1234!")
    fill_input(RegistrationPage.REPEAT_PASSWORD_INPUT, "Test1234!")

    # Крок 3: Надіслати форму
    click_element(RegistrationPage.REGISTER_BTN)

    # Крок 4: Перевірка повідомлення про успішну реєстрацію
    success_modal = wait.until(lambda d: d.find_element(*RegistrationPage.SUCCESS_MODAL))
    assert "Registration complete" in success_modal.text
