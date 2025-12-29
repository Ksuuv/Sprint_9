import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.general_locators import GeneralLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открытие урла')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step('Ожидание пока элемент не исчезнет')
    def wait_until_not_element_visible(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    @allure.step('Клик на элемент с ожиданием')
    def click_to_element(self, element):
        self.wait.until(ec.visibility_of_element_located(element))
        self.driver.find_element(*element).click()
    
    @allure.step('Заполнение поля текстом')
    def send_keys(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Извлечение текста из элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.find_element_with_wait(locator)

    @allure.step('Проверка что url содержит /signin')
    def url_contains_signin(self):
        self.wait.until(ec.url_contains('/signin'))

    @allure.step('Клик на кнопку Создать аккаунт')
    def click_create_account_btn(self):
        self.click_to_element(GeneralLocators.BTN_CREATE_ACCOUNT)

    @allure.step('Клик на кнопку Войти в хедере')
    def click_enter_btn_header(self):
        self.click_to_element(GeneralLocators.BTN_ENTER)

    @allure.step('Проверка что url содержит /recipes')
    def url_contains_recipes(self):
        self.wait.until(ec.url_contains('/recipes'))

    @allure.step('Поиск кнопки Выход в хедере')
    def find_exit_btn_header(self):
        return self.find_element(GeneralLocators.BTN_EXIT)
    
    @allure.step('Поиск кнопки Создать рецепт')
    def find_create_recipe_btn(self):
        self.find_element_with_wait(GeneralLocators.BTN_CREATE_RECIPES)

    @allure.step('Клик на кнопку Создать рецепт в хедере')
    def click_create_recipe_btn(self):
        self.click_to_element(GeneralLocators.BTN_CREATE_RECIPES)

    @allure.step('Клик на кнопку Создать аккаунт')
    def find_click_create_btn(self):
        self.click_to_element(GeneralLocators.BTN_CREATE_ACCOUNT)

    @allure.step('Скрипт чтобы сделать элемент видимым')
    def make_element_visible(self, element):
        self.driver.execute_script("arguments[0].style.display='block';", element)

    @allure.step('Нажать кнопку ESCAPE')
    def press_escape_btn(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()

    @allure.step('Переключение на окно с алертом браузера')
    def switch_to_alert(self):
        return self.driver.switch_to.alert