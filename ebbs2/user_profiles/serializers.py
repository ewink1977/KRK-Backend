from rest_framework import serializers
from .models import UserProfile

# PROFILE SERIALIZERS
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 1
        fields = ['user', 'position', 'bio', 'image', 'Post']
