from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer, UserSerializer


class CreateUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class PostDetail(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class LikePost(APIView):

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        post.save()
        return Response({'success': True}, status=status.HTTP_201_CREATED)
