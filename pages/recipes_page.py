import allure
from pages.base_page import BasePage
from locators.recipes_locators import RecipesLocators
from data import RecipeData


class RecipesPage(BasePage):


    @allure.step('Поиск тайтла Рецепты')
    def find_recipes_title(self):
        return self.find_element(RecipesLocators.TXT_TITLE_RECIPE)
    
    @allure.step('Поиск тайтла Рецепты c ожиданием')
    def find_recipes_title_with_wait(self):
        self.find_element_with_wait(RecipesLocators.TXT_RECIPES)

    @allure.step('Поиск тайтла Создание рецепта c ожиданием')
    def find_creating_recipes_title_with_wait(self):
        return self.find_element_with_wait(RecipesLocators.TXT_CREATING_RECIPE)

    @allure.step('Заполнение поля Название рецепта')
    def filling_recipe_name_field(self):
        self.send_keys(RecipesLocators.INPUT_RECIPE_NAME, RecipeData.recipe_data['name'])
    
    @allure.step('Заполнение поля Ингредиенты')
    def filling_ingredients_field(self):
        self.send_keys(RecipesLocators.INPUT_INGREDIENTS, RecipeData.recipe_data['ingredients'])

    @allure.step('Заполнение поля Граммы')
    def filling_ingr_gramm_field(self):
        self.send_keys(RecipesLocators.INPUT_INGR_GRAMM, RecipeData.recipe_data['ingr_gramm'])

    @allure.step('Заполнение поля Время приготовления')
    def filling_time_field(self):
        self.send_keys(RecipesLocators.INPUT_TIME, RecipeData.recipe_data['time'])

    @allure.step('Заполнение поля Описание рецепта')
    def filling_description_field(self):
        self.send_keys(RecipesLocators.INPUT_DESCRIPTION, RecipeData.recipe_data['desc'])

    @allure.step('Выбор ингредиента из списка')
    def choosing_ingredient(self):
        self.filling_ingredients_field()
        self.find_element_with_wait(RecipesLocators.DROPDOWN_ADD_INGR)
        self.click_to_element(RecipesLocators.DROPDOWN_ADD_INGR)
        self.wait_until_not_element_visible(RecipesLocators.DROPDOWN_ADD_INGR)

    @allure.step('Клик на кнопку Добавить ингредиент')
    def click_add_ingredient(self):
        self.find_element_with_wait(RecipesLocators.BTN_ADD_INGR)
        self.click_to_element(RecipesLocators.BTN_ADD_INGR)

    @allure.step('Скролл к кнопке Создать рецепт снизу')
    def scroll_to_create_recipe_bottom(self):
        self.scroll_to_element(RecipesLocators.BTN_CREATE_RECIPE)

    @allure.step('Загрузка картинки на сервер через поле Выбрать файл')
    def upload_image(self, text):
        file_input = self.find_element(RecipesLocators.INPUT_UPLOAD_FILE)
        self.make_element_visible(file_input)
        file_input.send_keys(text)
        self.press_escape_btn()

    @allure.step('Клик на кнопку Создать рецепт для создания рецепта')
    def click_create_recipe_bottom(self):
        self.click_to_element(RecipesLocators.BTN_CREATE_RECIPE)

    @allure.step('Поиск кнопки Редактировать рецепт')
    def find_edit_recipe_btn_with_wait(self):
        self.find_element_with_wait(RecipesLocators.BTN_EDIT_RECIPE)

    @allure.step('Получение текста из тайтла созданного рецепта')
    def get_text_from_title_recipe(self):
        return self.get_text(RecipesLocators.TXT_TITLE_RECIPE)