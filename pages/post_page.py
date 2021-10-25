import allure
from loguru import logger
from framework.BaseAdapter import BaseAdapter
from json_reader import JsonReader


class PostsPage(BaseAdapter):
    response = None

    def __init__(self):
        res = self.response

    @allure.step('Post post')
    def post_post(self, base_url, post_modal, status_code):
        self.response = self.post(base_url, post_modal, status_code)
        logger.info(self.response.text)

    @allure.step('Get all posts')
    def get_all_posts(self, base_url, status_code):
        self.response = self.get(base_url, status_code)
        logger.info(self.response.text)

    @allure.step('Get post')
    def get_post(self, base_url, id, status_code):
        self.response = self.get(base_url + id, status_code)
        logger.info(self.response.text)

    @allure.step('Created post validation')
    def validation_post_post(self, id, userid):
        post = self.response.json()

        with allure.step('Actual result'):
            print(self.response.text)

        if post['id'] == id:
            logger.info('Id is correct')

        if post['userId'] == userid:
            logger.info('userid is correct')

        if post['title'] and post['body'] is not "":
            logger.info("Title and body is not empty")

    @allure.step('Posts validation')
    def validation_all_posts(self):
        post = self.response.json()

        with allure.step('Expected result'):
            print(JsonReader().json_reader(
                'exected_result//posts.json'))

        assert post == JsonReader().json_reader('exected_result//posts.json'), \
            f'Actual post is not equal {post} '

        for item in self.response.json():
            assert item['id'] + 1 > item['id'], f"Posts' id is no correct"

    @allure.step('Post validation')
    def validation_post(self, status_code, number):
        post = self.response.json()

        if status_code != 404:

            with allure.step('Expected result'):
                print(JsonReader().json_reader_get_part(
                    'exected_result//posts.json', number))

            assert post == JsonReader().json_reader_get_part(
                'exected_result//posts.json', number), \
                f'Actual post is not equal {post}'
        else:

            with allure.step('Expected result'):
                print(JsonReader().json_reader('exected_result//error.json'))

            assert post == JsonReader().json_reader('exected_result//error.json'), \
                f'Actual post is not empty {post}'
