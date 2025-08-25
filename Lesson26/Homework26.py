from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# 1. Ініціалізація браузера
driver = webdriver.Chrome()
driver.get("http://localhost:5000/dz.html")

# Очікуваний текст успішної верифікації
expected_text = "Верифікація пройшла успішно!"


# Функція для перевірки фрейму
def verify_frame(frame_id, input_id, secret_text):
    # Переключення у фрейм
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    # Введення тексту
    input_element = driver.find_element(By.ID, input_id)
    input_element.clear()
    input_element.send_keys(secret_text)

    # Натискання кнопки
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    # Робота з alert
    alert = Alert(driver)
    time.sleep(1)  # Невелика пауза для появи alert
    alert_text = alert.text
    print(f"Фрейм: {frame_id}, Повідомлення: {alert_text}")

    # Перевірка тексту alert
    if alert_text == expected_text:
        print(f"[OK] Верифікація у {frame_id} пройшла успішно.")
    else:
        print(f"[FAIL] Верифікація у {frame_id} не пройшла.")

    alert.accept()  # Закриваємо alert
    driver.switch_to.default_content()  # Повертаємося на головну сторінку


# 2. Перевірка першого фрейму
verify_frame("frame1", "input1", "Frame1_Secret")

# 3. Перевірка другого фрейму
verify_frame("frame2", "input2", "Frame2_Secret")

# Закриваємо браузер
time.sleep(2)
driver.quit()
