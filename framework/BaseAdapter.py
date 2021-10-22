import requests as requests


class BaseAdapter:
    @staticmethod
    def post(base_url, post_Modal, status_code):
        response = requests.post(base_url, json=post_Modal)
        assert response.status_code == status_code

    @staticmethod
    def get(base_url, status_code, id, userid):
        response = requests.get(base_url)
        assert response.status_code == status_code
        post = response.json()
        assert post['id'] == id
        assert post['userId'] == userid

    def gets(self,base_url, status_code):
        response = requests.get(base_url)
        assert response.status_code == status_code
        post = response.json()

