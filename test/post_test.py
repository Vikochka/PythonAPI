from pages.post_page import PostsPage
from faker import Faker
import allure


@allure.feature('Create post')
def test_create_post():
    post_modal = {
        "userId": 1,
        "id": 101,
        "title": Faker().name(),
        "body": Faker().text()
    }
    p = PostsPage()
    p.post_post('https://jsonplaceholder.typicode.com/posts', post_modal, 201)
    p.validation_post_post(101, 1)


@allure.feature('Get error post')
def test_get_error_post():
    p = PostsPage()
    p.get_post('https://jsonplaceholder.typicode.com/posts/', '150', 404)
    p.validation_post(404, 150)


@allure.feature('Get all post')
def test_get_all_posts():
    p = PostsPage()
    p.get_all_posts('https://jsonplaceholder.typicode.com/posts/', 200)
    p.validation_all_posts()


@allure.feature('Get post')
def test_get_post():
    p = PostsPage()
    p.get_post('https://jsonplaceholder.typicode.com/posts/', '99', 200)
    p.validation_post(200, 99)
