from rest_framework import serializers
from .models import Post, PostReply

# POST SERIALIZERS
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

class PostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReply
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )

# Add Post Serializer
class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority', 'department', 'is_reply', 'created_at' )