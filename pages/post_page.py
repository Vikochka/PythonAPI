import requests
from loguru import logger
from framework.BaseAdapter import BaseAdapter
from json_reader import JsonReader


class PostsPage(BaseAdapter):
    response = None

    def __init__(self):
        res = self.response

    def post_post(self, base_url, post_Modal):
        self.response = requests.post(base_url, post_Modal)
        logger.info(self.response.text)

    def get_all_posts(self, base_url):
        self.response = requests.get(base_url)
        logger.info(self.response.text)

    def get_post(self, base_url, id):
        self.response = requests.get(base_url + id)
        logger.info(self.response.text)

    def validation_post_post(self, id, userid, status_code):
        post = self.response.json()
        logger.info(post)
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"
        assert post['id'] == id
        assert post['userId'] == userid
        if post['title'] and post['body'] is not "":
            logger.info("Title and body is not empty")
        assert self.response.status_code == status_code
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"

    def validation_all_posts(self, status_code):
        post = self.response.json()
        assert post == JsonReader().json_reader('E://iTechArt//Python//PythonAPI//exected_result//posts.json')
        assert self.response.status_code == status_code
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"
        for item in self.response.json():
            assert item['id'] + 1 > item['id']

    def validation_post(self, status_code, number):
        post = self.response.json()
        logger.info(post)
        assert self.response.headers["Content-type"] == "application/json; charset=utf-8"
        assert self.response.status_code == status_code
        if status_code != 404:
            assert post == JsonReader().json_reader_get_part(
                'E://iTechArt//Python//PythonAPI//exected_result//posts.json', number)
        else:
            assert post == JsonReader().json_reader('E://iTechArt//Python//PythonAPI//exected_result//error.json')
