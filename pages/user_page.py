import allure
from loguru import logger
from framework.BaseAdapter import BaseAdapter
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
    def validation_all_users(self):
        users = self.response.json()
        assert users == JsonReader().json_reader('exected_result//users.json')
        for items in users:
            assert users[5 - 1] == JsonReader().json_reader_get_part(
                'exected_result//users.json', 5), \
                f'Actual user is not equal {users}'

    @allure.step('User validation')
    def validation_user(self, status_code, number):
        users = self.response.json()
        if status_code != 404:
            assert users == JsonReader().json_reader_get_part(
                'exected_result//users.json', number), \
                f'Actual user is not equal {users}'
        else:
            assert users == JsonReader().json_reader('exected_result//error.json'), \
                f'Actual user is not empty {users}'
