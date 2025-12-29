import allure
from pages.base_page import BasePage
from locators.signup_locators import SignupLocators
from data import UserData


class SignupPage(BasePage):


    @allure.step('Поиск тайтла Регистрация')
    def find_registration_title(self):
        return self.find_element(SignupLocators.TXT_REGISTER)
    
    @allure.step('Заполнение поля Имя')
    def filling_name_field(self):
        self.send_keys(SignupLocators.INPUT_FIRST_NAME, UserData.user_data['first_name'])

    @allure.step('Заполнение поля Фамилия')
    def filling_lastname_field(self):
        self.send_keys(SignupLocators.INPUT_LAST_NAME, UserData.user_data['last_name'])

    @allure.step('Заполнение поля Имя пользователя')
    def filling_username_field(self):
        self.send_keys(SignupLocators.INPUT_USER_NAME, UserData.user_data['login'])

    @allure.step('Заполнение поля Адрес электронной почты')
    def filling_email_field(self):
        self.send_keys(SignupLocators.INPUT_EMAIL, UserData.user_data['email'])

    @allure.step('Заполнение поля Пароль')
    def filling_pass_field(self):
        self.send_keys(SignupLocators.INPUT_PASS, UserData.user_data['password'])

    @allure.step('Клик на кнопку Создать аккаунт')
    def click_create_account_btn(self):
        self.click_to_element(SignupLocators.BTN_CREATE_ACCOUNT)