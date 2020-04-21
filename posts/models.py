from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	pass


class Post(models.Model):
	author = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				related_name='author',
				on_delete=models.CASCADE,
	)
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(
				settings.AUTH_USER_MODEL,
				related_name='likes',
				blank=True,
	)

	def __str__(self):
		return f'{self.title}'