from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    PostViewSet is used for the CMS side of the website.
    This means that the endpoints generated from this viewset
    are not used to query the blog posts in jabbariao.com
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_published_posts_list(_request):
    posts = Post.objects.filter(published=True)
    serializer = PostListSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_published_post_detail(_request, pk):
    post = Post.objects.filter(published=True).get(pk=pk)
    serializer = PostDetailSerializer(post)

    return Response(serializer.data)
