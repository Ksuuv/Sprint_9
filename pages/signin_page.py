import allure
from pages.base_page import BasePage
from locators.signin_locators import SigninLocators
from selenium.webdriver.support import expected_conditions as ec
from data import UserData


class SigninPage(BasePage):


    @allure.step('Поиск формы авторизации')
    def find_auth_form(self):
        return self.find_element(SigninLocators.WDG_AUTH_FORM)

    @allure.step('Клик на кнопку Войти')
    def find_click_enter_btn(self):
        button = self.find_element(SigninLocators.BTN_ENTER)
        self.click_to_element(button)

    @allure.step('Заполнение поля Адрес электронной почты')
    def filling_email_field(self):
        self.send_keys(SigninLocators.INPUT_EMAIL, UserData.exist_user['email'])

    @allure.step('Заполнение поля Пароль')
    def filling_pass_field(self):
        self.send_keys(SigninLocators.INPUT_PASS, UserData.exist_user['pass'])

    @allure.step('Заполнение логина в поле Адрес электронной почты')
    def filling_login(self):
        self.send_keys(SigninLocators.INPUT_EMAIL, UserData.exist_user['login'])

    @allure.step('Клик на кнопку Войти в форме авторизации')
    def click_enter_btn(self):
        self.click_to_element(SigninLocators.BTN_ENTER)

    @allure.step('Поиск всплывающего алерта браузера и получение текста из него')
    def find_alert_popup_and_get_text(self):
        self.wait.until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text
