from django.shortcuts import render
from django.conf import settings
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
# Core
from .serializer import *
from .models import *
from .ai_module import generate_financial_report
# Restframework
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.permissions import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

@login_required
def generate_report_view(request):
    user = request.user
    report_text = generate_financial_report(user)
    data = FinancialReport.objects.create(user=user, report_name="AI Generated Report", report_data={'summary': report_text})
    response = JsonResponse(data, status=200)
    
    return response
