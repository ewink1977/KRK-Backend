from .models import Post, PostReply
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, PostReplySerializer

# POST VIEWSET
class AllPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_reply = False)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class AllReplyViewSet(viewsets.ModelViewSet):
    queryset = PostReply.objects.filter(is_reply = True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostReplySerializer