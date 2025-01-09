from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    email=serializers.EmailField()

    def validation_email(self,value):
        if "@" not in value:
            raise serializers.ValidationError("The Email must contain '@'.")
        return value
    def create(self,validated_data):
        return User.objects.create(**validated_data)
