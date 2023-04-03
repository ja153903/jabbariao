from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "created_at", "updated_at")


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "updated_at")