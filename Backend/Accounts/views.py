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

#** Create User Object View
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]