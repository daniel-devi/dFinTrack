from django.contrib.auth.models import User
# Accounts

# Restframework
from rest_framework import serializers
# Create Your Serializer

# User Model Serializer Class {A Api Format of the Model}
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}, "date_joined": {"read_only": True}}