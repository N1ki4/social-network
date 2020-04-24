from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("signup")
CREATE_TOKEN_URL = reverse("login")


class UserEndpoints(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_create_user_success(self):
        payload = {
            "email": "test@uuu.kkk.cc",
            "username": "testusername",
            "password": "testpwd1234"
        }
        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**resp.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', resp.data)
    
    def test_user_already_exists(self):
        payload = {
            "email": "test@uuu.kkk.cc",
            "username": "testsss",
            "password": "testpwd1234"
        }
        User.objects.create(**payload)
        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_token(self):
        create_user_payload = {
            "email":"test@uuu.ccc.kk",
            "username":"sometestname", 
            "password":"pswd12345",
        }
        resp1 = self.client.post(CREATE_USER_URL, create_user_payload)
        payload = {
            "username": "sometestname",
            "password": "pswd12345"
        }
        resp2 = self.client.post(CREATE_TOKEN_URL, payload)
        self.assertIn("token", resp2.data)
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
    
    def test_create_token_invalid_credentials(self):
        User.objects.create(
            email = "test@uuu.kkk.cc",
            username = "testsss",
            password = "testpwd1234"
        )
        payload = {
            "username": "test1234",
            "password": "testss123",
        }
        resp = self.client.post(CREATE_TOKEN_URL, payload)
        self.assertNotIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)