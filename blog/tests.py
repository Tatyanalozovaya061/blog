from django.test import TestCase
from blog.models import Blog
from users.models import User


class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone='1234567890', password='test')
        self.post = Blog.objects.create(title='test', content='test', owner=self.user)

        def test_blog_creation(self):
            post = Blog.objects.create(title='test2', content='test2', owner=self.user)
            self.assertEqual(post.title, 'test2')
            self.assertEqual(post.content, 'test2')
            self.assertEqual(post.owner, self.user)
