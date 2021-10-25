from pages.post_page import PostsPage


def test_create_post():
    postModal = {
        "userId": 1,
        "id": 101,
        "title": "temporibus sit alias delectus eligendi possimus magni",
        "body": "quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque "
                "dolorem quia "
    }
    p = PostsPage()
    p.post_post('https://jsonplaceholder.typicode.com/posts', postModal)
    p.validation_post_post(101, '1', 201)


def test_get_error_post():
    p = PostsPage()
    p.get_post('https://jsonplaceholder.typicode.com/posts/', '150')
    p.validation_post(404, 150)


def test_get_all_posts():
    p = PostsPage()
    p.get_all_posts('https://jsonplaceholder.typicode.com/posts/')
    p.validation_all_posts(200)


def test_get_post():
    p = PostsPage()
    p.get_post('https://jsonplaceholder.typicode.com/posts/', '99')
    p.validation_post(200, 99)
