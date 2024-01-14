from unittest import TestCase
from source.blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        b = Blog('Test','Test author',4)

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test','Test author',4)
        b.posts = [1]
        b1 = Blog('My post', 'Artur',4)
        b1.posts = ["post1", 'post2']

        self.assertEqual(b.__repr__(), 'Test by Test author (1 post)')
        self.assertEqual(b1.__repr__(), 'My post by Artur (2 posts)')





