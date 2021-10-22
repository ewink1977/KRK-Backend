from rest_framework import serializers
from .models import Post, PostReply
from django.contrib.auth.models import User

# Our PostSerializer needs to contain UserProfile information so that we can properly display the Post component on the front end!
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('id', 'username', 'first_name', 'last_name', 'userProfile')
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at'
            )

class PostReplySerializer(serializers.ModelSerializer):
    author_info = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = PostReply
        fields = ('id', 'author_info', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

# Add Post Serializer
class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )
