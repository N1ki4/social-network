from django.urls import path

from .views import PostList, PostDetail, CreateUser, LikePost
from rest_framework.authtoken import views


urlpatterns = [
    # Posts endpoints
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post_detail"),

    # User management endpoints
    path("user/create/", CreateUser.as_view(), name="signup"),
    path("user/token/", views.obtain_auth_token, name="login"),
    # Likes endpoint
    path('posts/<int:pk>/like/', LikePost.as_view(), name='like_post'),
]