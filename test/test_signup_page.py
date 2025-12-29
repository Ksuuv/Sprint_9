import allure
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
import urls


class TestSignupPage:

    @allure.title('Заполнение формы регистрации и создание аккаунта')
    def test_create_account(self, driver):
        signup_page = SignupPage(driver)
        signin_page = SigninPage(driver)

        signup_page.open_url(f'{urls.base_url}{urls.signup_url}')
        signup_page.filling_name_field()
        signup_page.filling_lastname_field()
        signup_page.filling_username_field()
        signup_page.filling_email_field()
        signup_page.filling_pass_field()
        signup_page.click_create_account_btn()
        signin_page.url_contains_signin()
        
        assert signin_page.find_auth_form(), 'Не нашли форму авторизации'