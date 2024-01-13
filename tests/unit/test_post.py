from unittest import TestCase
from source.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('test', 'test content')

        self.assertEqual('test', p.title)
        self.assertEqual('test content', p.content)


    def test_json(self):
        p = Post('test1', 'test1 content')
        expected = {'title': 'test1', 'content': 'test1 content'}

        self.assertEqual(expected,p.json())