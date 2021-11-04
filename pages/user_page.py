import allure
from loguru import logger
from framework.BaseAdapter import BaseAdapter
from framework.property_reader import PropertyReader
from json_reader import JsonReader


class UserPage(BaseAdapter):
    response = None

    def __init__(self):
        res = self.response

    @allure.step('Get all users')
    def get_all_users(self, base_url, status_code):
        self.response = self.get(base_url, status_code)
        logger.info(self.response.text)

    @allure.step('Get one user')
    def get_user(self, base_url, id, status_code):
        self.response = self.get(base_url + id, status_code)
        logger.info(self.response.text)

    @allure.step('Users validation')
    def validation_all_users(self,id):
        users = self.response.json()
        assert users == JsonReader().json_reader('exected_result//users.json')
        for items in users:
            assert users[id - 1] == JsonReader().json_reader_get_part(
                'exected_result//users.json', id), \
                f'Actual user is not equal {users}'

    @allure.step('User validation')
    def validation_user(self, status_code, number):
        users = self.response.json()

        if status_code != PropertyReader().get_property('..//config.properties', 'error.status'):

            with allure.step('Expected result'):
                print(JsonReader().json_reader_get_part(
                    'exected_result//users.json', number))

            assert users == JsonReader().json_reader_get_part(
                'exected_result//users.json', number), \
                f'Actual user is not equal {users}'
        else:
            with allure.step('Expected result'):
                print(JsonReader().json_reader_get_part(
                    'exected_result//error.json', number))

            assert users == JsonReader().json_reader('exected_result//error.json'), \
                f'Actual user is not empty {users}'
