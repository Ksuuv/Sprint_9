from selenium.webdriver.common.by import By


class GeneralLocators:

    BTN_CREATE_ACCOUNT = By.XPATH, '//*[text()="Создать аккаунт"]'
    BTN_CREATE_RECIPES = By.XPATH, '//*[text()="Создать рецепт"]'
    BTN_ENTER = By.XPATH, '//a[text()="Войти"]'
    BTN_EXIT = By.XPATH, '//*[text()="Выход"]'
    