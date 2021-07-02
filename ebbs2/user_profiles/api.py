from .models import UserProfile
from rest_framework import viewsets, permissions
from .serializers import UserProfileSerializer

# USER PROFILE VIEWSET
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer