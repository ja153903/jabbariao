from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    PostViewSet is only used for the CMS side of my personal website.

    This should not be used for querying posts in the actual website
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer


@api_view(["GET"])
def get_published_posts_list(_request):
    posts = Post.objects.filter(published=True)
    serializer = PostListSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_published_post_detail(_request, pk):
    post = Post.objects.filter(published=True).get(pk=pk)
    serializer = PostDetailSerializer(post)

    return Response(serializer.data)
