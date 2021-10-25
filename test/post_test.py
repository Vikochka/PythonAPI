from pages.post_test import PostsPage


def test_create_post():
    postModal = {
        "userId": 1,
        "id": 101,
        "title": "temporibus sit alias delectus eligendi possimus magni",
        "body": "quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque "
                "dolorem quia "
    }
    p = PostsPage()
    p.post_post('https://jsonplaceholder.typicode.com/posts', postModal, 201)
    p.validation_post_post(101, '1')
