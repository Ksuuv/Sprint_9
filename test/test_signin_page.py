import allure
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.recipes_page import RecipesPage
import data
import urls


class TestSigninPage:

    @allure.title('По тапу на кнопку Создать аккаунт открывается форма регистрации')
    def test_tap_create_btn_open_registration(self, driver):
        signin_page = SigninPage(driver)
        signup_page = SignupPage(driver)

        signin_page.find_click_create_btn()

        assert signup_page.find_registration_title(), 'Не нашли тайтл Регистрация'

    @allure.title('По тапу на кнопку Войти открывается страница авторизации')
    def test_tap_enter_btn_open_auth_page(self, driver):
        signin_page = SigninPage(driver)
        recipes_page = RecipesPage(driver)

        recipes_page.open_url(f'{urls.base_url}{urls.recipes_url}')
        recipes_page.find_recipes_title_with_wait()
        recipes_page.click_enter_btn_header()
        
        assert signin_page.find_auth_form(), 'Не нашли форму авторизации'

    @allure.title('При авторизации с email открывается алерт в браузере')
    def test_auth_with_email_open_alert(self, driver):
        signin_page = SigninPage(driver)

        signin_page.filling_email_field()
        signin_page.filling_pass_field()
        signin_page.click_enter_btn()

        assert signin_page.find_alert_popup_and_get_text() == data.alert_text, 'Алерт не появился или имеет другой текст'

    @allure.title('При авторизации с логином вместо email происходит авторизация пользователя')
    def test_auth_with_login_open_main(self, driver):
        signin_page = SigninPage(driver)
        recipes_page = RecipesPage(driver)

        signin_page.filling_login()
        signin_page.filling_pass_field()
        signin_page.click_enter_btn()
        recipes_page.url_contains_recipes()
        
        assert recipes_page.find_exit_btn_header(), 'Кнопка выход не найдена'