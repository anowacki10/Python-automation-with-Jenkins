from source.post import Post

class Blog:
    def __init__(self, title, author, max_posts):

        self.title = title
        self.author = author
        self.posts = []
        self.max_posts = max_posts

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title, self.author, len(self.posts), 's' if len(self.posts) > 1 else '')
    def create_post(self, title, content):
        if len(self.posts) < self.max_posts:
            self.posts.append(Post(title,content))
        else:
            raise ValueError("The maximum amount of posts has been reached")

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }


