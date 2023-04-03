from rest_framework import viewsets

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer
