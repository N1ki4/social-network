from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Post
from ..serializers import PostSerializer

from rest_framework.test import APIClient
from rest_framework import status


POST_URL = reverse("post_list")


def detail_url(post_id):
    return reverse("post_detail", args=[post_id])

def post_like_url(post_id):
    return reverse("like_toggle", args=[post_id])

class PublicPostEndpoints(TestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        resp = self.client.get(POST_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePostEndpoints(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password="testpswrd",
            email="testmail@nikita.com"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
    
    def test_create_post(self):
        payload = {
            "title": "test_title",
            "body": "test body exapmple text",
        }

        resp = self.client.post(POST_URL, payload)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_retrieve_posts(self):
        post1 = Post.objects.create(
            title="test_title",
            body="test body exapmple text",
            author=self.user,
        )
        post2 = Post.objects.create(
            title="test_title222",
            body="test body exapmple text2222",
            author=self.user,
        )

        resp = self.client.get(POST_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    
    def test_detail_post(self):
        post = Post.objects.create(
            title="test_title",
            body="test body exapmple text",
            author=self.user,
        )
        url = detail_url(post.id)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    
    def test_like_toggle(self):
        post = Post.objects.create(
            title="test_title",
            body="test body exapmple text",
            author=self.user,
        )
        url = post_like_url(post.id)
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn(self.user.id, resp.data)

        post.refresh_from_db()
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertNotIn(self.user.id, resp.data)