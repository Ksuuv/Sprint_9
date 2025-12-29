from selenium.webdriver.common.by import By


class SigninLocators:

    TXT_SITE_ENTER = By.XPATH, '//h1[text()="Войти на сайт"]'
    WDG_AUTH_FORM = By.XPATH, '//*[contains(@class, "styles_form")]'
    BTN_ENTER = By.XPATH, '//button[text()="Войти"]'
    INPUT_EMAIL = By.XPATH, '//*[@name="email"]'
    INPUT_PASS = By.XPATH, '//*[@name="password"]'