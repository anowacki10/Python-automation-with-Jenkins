from unittest import (TestCase, )
from unittest.mock import patch
from source import app
from source.blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test author',4)
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('-Test by Test author (0 post)')
