import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    options = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def click_element(driver, wait):
    def _click(locator):
        elem = wait.until(EC.element_to_be_clickable(locator))
        elem.click()
    return _click


@pytest.fixture
def fill_input(driver, wait):
    def _fill(locator, text):
        elem = wait.until(EC.presence_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)
    return _fill
