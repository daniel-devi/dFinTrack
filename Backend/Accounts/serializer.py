from django.contrib.auth.models import User
# Accounts

# Restframework
from rest_framework import serializers


#? Create Your Serializer

# Serializer for User Model: Serializes user data for API responses and requests
class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed user information including sensitive fields.
    This serializer is used for displaying and interacting with user data.
    """
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "date_joined"]
        extra_kwargs = {
            "password": {"write_only": True},  # Password should be write-only
            "date_joined": {"read_only": True}  # Date joined should be read-only
        }

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
        Hashes the password before saving the user.
        """
        # Creating a user with hashed password
        user = User.objects.create_user(**validated_data)
        return user



# Serializer for Username: Serializes only the username field
class UsernameSerializer(serializers.ModelSerializer):
    """
    Serializer for user usernames only. This is useful for operations where 
    only the username is needed, like username-based queries.
    """
    class Meta:
        model = User
        fields = ['username']



# Serializer for updating user profiles: Allows updating user profile fields
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user profiles. It includes validations for email uniqueness.
    """
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},  # First name is required
            'last_name': {'required': True},   # Last name is required
            'email': {'required': True},       # Email is required
        }

    def validate_email(self, value):
        """
        Validate that the email is unique across all users.
        Raises a validation error if the email is already in use by another user.
        """
        # Get the current user from request context
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        """
        Update the user instance with the provided validated data.
        Updates first name, last name, and email fields.
        """
        # Updating user instance with new data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
