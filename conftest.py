import pytest
import os
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.options import Options
import urls
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage


@pytest.fixture(scope='function')
def driver():
    if os.getenv('SELENIUM_HUB_URL'):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Remote(command_executor=os.getenv('SELENIUM_HUB_URL'), options=chrome_options)
        base_url = os.getenv('BASE_URL', 'https://foodgram-frontend-1.prakticum-team.ru')
    else:
        driver = webdriver.Chrome()
        base_url = urls.base_url
    
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def auth_user(driver):
    signin_page = SigninPage(driver)
    recipes_page = RecipesPage(driver)

    signin_page.filling_login()
    signin_page.filling_pass_field()
    signin_page.click_enter_btn()
    recipes_page.find_create_recipe_btn()

    return driver

@pytest.fixture
def get_absolute_image_path():
    project_root = Path(__file__).parent
    image_path = project_root / "assets" / "cat.jpg"

    return str(image_path.absolute())