from helpers import HelpfullMethods


class UserData:

    user_data = {
        'first_name':f'{HelpfullMethods.first_name}',
        'last_name':f'{HelpfullMethods.last_name}',
        'login':f'{HelpfullMethods.login}',
        'email':HelpfullMethods.generate_random_email(),
        'password':f'{HelpfullMethods.password}'
        }
    
    exist_user = {
        'email':'alex_cat@yandex.ru',
        'pass':'catpassword',
        'login':'alex_cat'
    }

class RecipeData:

    recipe_data = {
        'name':'Рецепт от шеф-повара',
        'ingredients':'блинная мука',
        'ingr_gramm':'900',
        'time':'600',
        'desc':'Изумительный рецепт от шеф_повара'
    }

alert_text = 'Невозможно войти с предоставленными учетными данными.'