from unittest import TestCase
from source.blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test author',4)
        for _ in range(4):
            b.create_post('post title', 'post content')

        self.assertEqual(len(b.posts), 4)
        self.assertEqual(b.posts[3].title, 'post title')
        self.assertEqual(b.posts[3].content, 'post content')

    def test_overload_posts_in_blog(self):
        b = Blog('Test', 'Test author',4)
        for _ in range(4):
            b.create_post('new post', 'post content')

        with self.assertRaises(ValueError):  # Error raised, negative test
            for _ in range(10):
                b.create_post('overload post', 'too many posts')

        self.assertEqual(len(b.posts), b.max_posts)
        self.assertEqual(b.posts[3].title, 'new post')
        self.assertEqual(b.posts[3].content, 'post content')

    def test_blog_json(self):
        b = Blog('Test', 'Test author',4)
        for _ in range(4):
            b.create_post('post title', 'post content')

        expected = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [
                {'content': 'post content', 'title': 'post title'},
                {'content': 'post content', 'title': 'post title'},
                {'content': 'post content', 'title': 'post title'},
                {'content': 'post content', 'title': 'post title'},

            ]
        }

        self.assertDictEqual(expected, b.json())

    def test_blog_json_with_no_posts(self):
        b = Blog('Test', 'Test author', 4)

        self.assertEqual(b.json(), {'author': 'Test author', 'posts': [], 'title': 'Test'})


