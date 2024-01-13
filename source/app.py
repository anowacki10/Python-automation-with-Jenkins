blogs = {}  # blog_name : blog objects

def menu():
    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('-{}'.format(blog))
