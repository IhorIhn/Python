from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)  # більше часу для очікування

    TRACKING_INPUT = (By.ID, "en")
    STATUS_CONTAINER = (By.CSS_SELECTOR, ".header__parcel-dynamic-status")
    STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")

    def open(self):
        self.driver.get(self.URL)

    def enter_tracking_number(self, number: str):
        input_field = self.wait.until(EC.element_to_be_clickable(self.TRACKING_INPUT))
        input_field.click()
        input_field.clear()
        input_field.send_keys(number)
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)

    def get_parcel_status(self) -> str:
        container = self.wait.until(EC.visibility_of_element_located(self.STATUS_CONTAINER))
        status_element = container.find_element(*self.STATUS_TEXT)
        return status_element.text.strip()  # видаляємо зайві пробіли
