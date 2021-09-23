from rest_framework.response import Response
from .models import Post, PostReply
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, PostReplySerializer, AddPostSerializer

# POST VIEWSET  
class AllPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_reply = False).order_by('created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class AllReplyViewSet(viewsets.ModelViewSet):
    queryset = PostReply.objects.filter(is_reply = True).order_by('created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostReplySerializer

class AddPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        queryset = Post.objects.filter(is_reply = False).order_by('created_at')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return queryset

class SinglePostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
        ]

    def get(self, request, pk):
        single_post = Post.objects.get(pk=pk)
        serializer = PostSerializer(single_post)
        return Response(serializer.data)

    def delete(self, request, pk):
        single_post = Post.objects.get(pk=pk)
        single_post.destroy()
        return Response