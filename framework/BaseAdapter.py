import requests as requests
import allure


class BaseAdapter:

    @staticmethod
    def post(base_url, post_modal, status_code):
        with allure.step("Send post request"):
            response = requests.post(base_url, json=post_modal)
            assert response.status_code == status_code
            assert response.headers["Content-type"] == "application/json; charset=utf-8"
            return response

    @staticmethod
    def get(base_url, status_code):
        with allure.step("Send get request"):
            response = requests.get(base_url)
            assert response.status_code == status_code
            assert response.headers["Content-type"] == "application/json; charset=utf-8"
            return response
