import allure
import random
import string


class HelpfullMethods:

    def generate_random_email():
        return f'tester{random.randint(100, 999)}@yandex.ru'

    @allure.step('Метод для генерации строк')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    user_data = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    last_name = generate_random_string(10)

    user_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
        "lastName": last_name
    }

