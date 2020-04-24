from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Post


class PostTests(TestCase):
    def setUp(self):
        User.objects.create(
            username="Sarah", 
            password="pass1234", 
            email="sarah@kkk.gg"
        )

    def test_post_str(self):
        post = Post.objects.create(
            title="My test title",
            body="Lorem ipsum dolor sit amet, \
                  consectetur adipiscing elit, sed do eiusmod \
                  tempor incididunt ut labore et dolore magna aliqua.",
            author=User.objects.get(username="Sarah")
        )

        self.assertEqual(str(post), post.title)