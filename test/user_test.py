from pages.user_page import UserPage


def test_get_all_users():
    p = UserPage()
    p.get_all_users('https://jsonplaceholder.typicode.com/users/', 200)
    p.validation_all_users()


def test_get_user():
    p = UserPage()
    p.get_user('https://jsonplaceholder.typicode.com/users/', '5', 200)
    p.validation_user(200, 5)
