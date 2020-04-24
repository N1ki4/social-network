from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post

from rest_framework.test import APIClient
from rest_framework import status


#CREATE_POST_URL = reverse("post_list")
#POST_DETAIL_URL = reverse("post_detail", args=[str(id)])
