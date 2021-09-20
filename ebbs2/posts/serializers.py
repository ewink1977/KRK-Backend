from rest_framework import serializers
from .models import Post, PostReply
from django.contrib.auth.models import User

# Post Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('id', 'username', 'first_name', 'last_name', 'userProfile' )


# POST SERIALIZERS
class PostSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

class PostReplySerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True)
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = PostReply
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )