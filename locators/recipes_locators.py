from selenium.webdriver.common.by import By


class RecipesLocators:

    TXT_RECIPES = By.XPATH, '//h1[text()="Рецепты"]'
    BTN_EXIT = By.XPATH, '//*[text()="Выход"]'
    TXT_CREATING_RECIPE = By.XPATH, '//h1[text()="Создание рецепта"]'
    INPUT_RECIPE_NAME = By.XPATH, '//*[text()="Название рецепта"]/following-sibling::input'
    INPUT_INGREDIENTS = By.XPATH, '//*[text()="Ингредиенты"]/following-sibling::input'
    INPUT_INGR_GRAMM = By.XPATH, '//*[contains(@class, "styles_ingredientsAmountValue")]'
    INPUT_TIME = By.XPATH, '//*[text()="Время приготовления"]/following-sibling::input'
    INPUT_DESCRIPTION = By.XPATH, '//*[contains(@class, "styles_textareaField")]'
    INPUT_UPLOAD_FILE = By.XPATH, '//input[@type="file"]'
    BTN_CREATE_RECIPE = By.XPATH, '//button[text()="Создать рецепт"]'
    BTN_ADD_INGR = By.XPATH, '//*[text()="Добавить ингредиент"]'
    BTN_EDIT_RECIPE = By.XPATH, '//*[text()="Редактировать рецепт"]'
    TXT_TITLE_RECIPE = By.XPATH, '//*[contains(@class, "styles_single-card__title")]'
    DROPDOWN_ADD_INGR = By.XPATH, '//*[text()="блинная мука"]'