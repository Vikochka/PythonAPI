from pages.user_page import UserPage


def test_get_all_users():
    p = UserPage()
    p.get_all_users('https://jsonplaceholder.typicode.com/users/')
    p.validation_all_users(200)


def test_get_user():
    p = UserPage()
    p.get_post('https://jsonplaceholder.typicode.com/users/', '5')
    p.validation_user(200, 5)
