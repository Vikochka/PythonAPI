from pages.post_test import PostsPage


def test_create_post():
    p = PostsPage()
    p.post_post('https://jsonplaceholder.typicode.com/posts')
    p.validation(201)