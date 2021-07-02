from rest_framework import serializers
from .models import UserProfile

# PROFILE SERIALIZERS
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'position', 'bio', 'image']
