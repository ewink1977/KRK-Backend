from rest_framework import serializers
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from .models import UserProfile

# PROFILE SERIALIZERS
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 1
        fields = ['user', 'position', 'bio', 'image']

# POST-AUTHOR SERIALIZERS 
# This data is needed to properly display posts.
class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'department', 'access_level']

class AuthorSerializer(serializers.ModelSerializer):
    userProfile = userProfileSerializer()
    class Meta:
        model = User
        depth = 1
        fields = ['id', 'username', 'first_name', 'last_name', 'userProfile']