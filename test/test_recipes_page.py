import allure
from pages.recipes_page import RecipesPage
from data import RecipeData


class TestRecipesPage:

    @allure.title('Переход по кнопке Создать рецепт авторизованным пользователем')
    def test_tap_create_recipe_btn_main(self, auth_user):
        recipes_page = RecipesPage(auth_user)

        recipes_page.click_create_recipe_btn()

        assert recipes_page.find_creating_recipes_title_with_wait(), 'Тайтл Рецепты не найден'

    @allure.title('Можно создать рецепт, заполнив все поля')
    def test_creating_recipe(self, auth_user, get_absolute_image_path):
        recipes_page = RecipesPage(auth_user)

        recipes_page.click_create_recipe_btn()
        recipes_page.find_creating_recipes_title_with_wait()
        recipes_page.filling_recipe_name_field()
        recipes_page.choosing_ingredient()
        recipes_page.filling_ingr_gramm_field()
        recipes_page.filling_time_field()
        recipes_page.filling_description_field()
        recipes_page.upload_image(get_absolute_image_path)
        recipes_page.scroll_to_create_recipe_bottom()
        recipes_page.click_add_ingredient()
        recipes_page.click_create_recipe_bottom()
        recipes_page.find_edit_recipe_btn_with_wait()

        assert recipes_page.get_text_from_title_recipe() == RecipeData.recipe_data['name'], 'Название рецепта не совпадает'