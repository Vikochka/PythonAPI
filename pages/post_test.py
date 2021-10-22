from multiprocessing import Value

import requests

from framework.BaseAdapter import BaseAdapter


class PostsPage(BaseAdapter):
    response = None

    def post_post(self, base_url):
        postModal = {
            "userId": 1,
            "id": 101,
            "title": "temporibus sit alias delectus eligendi possimus magni",
            "body": "quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque "
                    "dolorem quia "
        }
        base_url = base_url
        self.response = requests.post(base_url, json=postModal)
        return self.response

    def validation(self, status_code):
        assert self.response.status_code == status_code
