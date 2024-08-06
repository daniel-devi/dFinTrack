from django.conf import settings
from django.http import Http404, JsonResponse
# Accounts
from .serializer import *
from .models import *
# Restframework
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.permissions import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class CreateUserView(generics.CreateAPIView): 
    # Creates User using the Generic Create Username View
    queryset = User.objects.all() 
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

class UserDetailByIdView(generics.ListAPIView):
    """
    Retrieve a specific users based on their ID.
    """
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        """
        Filter users by ID based on the `ids` URL parameter.
        """
        user_id = self.kwargs['ids']
        return User.objects.filter(id__icontains=user_id)


class UserDetailByEmailView(generics.ListAPIView):
    """
    Retrieve a list of users based on their email address Using the Generic ListView.
    """
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]  # No specific permissions required for this view

    def get_queryset(self):
        """
        Filter users by email based on the `email` URL parameter.
        """
        email = self.kwargs['email']
        return User.objects.filter(email=email)


class UserListViewByUsername(generics.ListAPIView):
    """
    Retrieve a list of all users with only their usernames.
    """
    serializer_class = UsernameSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Open access to this view for all users
    