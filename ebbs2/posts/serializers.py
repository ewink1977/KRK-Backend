from rest_framework import serializers
from .models import Post, PostReply
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

# User Profile Serializer
class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'department', 'access_level']

# Post Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    userProfile = userProfileSerializer()
    class Meta:
        model = User
        depth = 1
        fields = ['id', 'username', 'first_name', 'last_name', 'userProfile']


# POST SERIALIZERS
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

class PostReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = PostReply
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

# Add Post Serializer
class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )