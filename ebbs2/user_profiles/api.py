from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import AuthorSerializer, UserProfileSerializer

# USER PROFILE VIEWSET
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer

class AllAuthorData(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [
        permissions.AllowAny
        ]

class PostAuthorData(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [
        permissions.AllowAny
        ]

    def get(self, request, pk):
        post_author = User.objects.get(pk=pk)
        serializer = AuthorSerializer(post_author)
        return Response(serializer.data)