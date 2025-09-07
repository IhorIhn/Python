from selenium.webdriver.common.by import By

class RegistrationPage:
    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPEAT_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BTN = (By.XPATH, "//button[contains(text(), 'Register')]")
    SUCCESS_MODAL = (By.XPATH, "//app-alert-list[contains(., 'Registration Complete')]")

