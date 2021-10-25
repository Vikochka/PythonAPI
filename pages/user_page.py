import requests
from loguru import logger
from framework.BaseAdapter import BaseAdapter
from json_reader import JsonReader


class UserPage(BaseAdapter):
    response = None

    def __init__(self):
        res = self.response

    def get_all_users(self, base_url):
        self.response = requests.get(base_url)
        logger.info(self.response.text)

    def get_post(self, base_url, id):
        self.response = requests.get(base_url + id)
        logger.info(self.response.text)

    def validation_all_users(self, status_code):
        posts = self.response.json()
        assert posts == JsonReader().json_reader('E://iTechArt//Python//PythonAPI//exected_result//users.json')
        assert self.response.status_code == status_code
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"
        for items in posts:
            assert posts[5 - 1] == JsonReader().json_reader_get_part(
                'E://iTechArt//Python//PythonAPI//exected_result//users.json', 5)

    def validation_user(self, status_code, number):
        post = self.response.json()
        logger.info(post)
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"
        assert self.response.status_code == status_code
        if status_code != 404:
            assert post == JsonReader().json_reader_get_part(
                'E://iTechArt//Python//PythonAPI//exected_result//users.json', number)
        else:
            assert post == JsonReader().json_reader('E://iTechArt//Python//PythonAPI//exected_result//error.json')
