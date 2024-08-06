from django.shortcuts import render
from django.conf import settings
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
# Core
from .serializer import *
from .models import *
from .ai_module import generate_financial_report
# Restframework
from rest_framework import viewsets
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

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing ExpenseCategory instances."""
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Transaction instances."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Budget instances."""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class FinancialGoalViewSet(viewsets.ModelViewSet):
    """ViewSet for managing FinancialGoal instances."""
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Notification instances."""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class UpdateViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Update instances."""
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class FinancialAnalyticsViewSet(viewsets.ModelViewSet):
    """ViewSet for managing FinancialAnalytics instances."""
    queryset = FinancialAnalytics.objects.all()
    serializer_class = FinancialAnalyticsSerializer

    def perform_update(self, serializer):
        """Update financial analytics after saving."""
        instance = serializer.save()
        instance.update_analytics()

class FinancialReportViewSet(viewsets.ModelViewSet):
    """ViewSet for managing FinancialReport instances."""
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer

    def perform_create(self, serializer):
        """Generate report data before saving."""
        instance = serializer.save()
        instance.generate_report()
