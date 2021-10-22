from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, PostReply
from rest_framework import generics, viewsets, permissions
from .serializers import PostSerializer, PostReplySerializer, AddPostSerializer


class AllPosts(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(is_reply=False).order_by('created_at')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class AddPostAPI(generics.CreateAPIView):
    serializer_class = AddPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            instance_serializer = PostSerializer(instance)
            return Response(instance_serializer.data)
        return Response(serializer.errors)
