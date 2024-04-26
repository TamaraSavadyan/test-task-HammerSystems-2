from rest_framework import serializers
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number']

class UserAuthenticationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    auth_code = serializers.CharField(required=True)

