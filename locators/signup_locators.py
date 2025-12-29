from selenium.webdriver.common.by import By


class SignupLocators:

    TXT_REGISTER = By.XPATH, '//h1[text()="Регистрация"]'
    INPUT_FIRST_NAME = By.XPATH, '//*[@name="first_name"]'
    INPUT_LAST_NAME = By.XPATH, '//*[@name="last_name"]'
    INPUT_USER_NAME = By.XPATH, '//*[@name="username"]'
    INPUT_EMAIL = By.XPATH, '//*[@name="email"]'
    INPUT_PASS = By.XPATH, '//*[@name="password"]'
    BTN_CREATE_ACCOUNT = By.XPATH, '//button[text()="Создать аккаунт"]'
    