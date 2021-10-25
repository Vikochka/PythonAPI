from multiprocessing import Value

import requests
from  loguru import logger
from framework.BaseAdapter import BaseAdapter


class PostsPage(BaseAdapter):
    response = None

    def __init__(self):
        res = self.response

    def post_post(self, base_url, post_Modal, status_code):
        base_url = base_url
        self.response = requests.post(base_url, post_Modal, status_code)
        logger.info(self.response)

    def validation_post_post(self, id, userid):
        post = self.response.json()
        logger.info(post)
        assert post['id'] == id
        assert post['userId'] == userid

    def validation_all_posts(self, status_code):
        assert self.response.status_code == status_code
        print(self.response)
        for item in self.response.json():
            assert item['id'] + 1 > item['id']
