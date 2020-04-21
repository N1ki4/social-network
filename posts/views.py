from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    serializer_class = PostSerializer
    def post(self, request):
        serizlier = PostSerializer(data=request.data)
        if serizlier.is_valid():
            serizlier.save()
            return Response(serizlier.data, status=status.HTTP_201_CREATED)
        return Response(serizlier.errors, status=status.HTTP_400_BAD_REQUEST)