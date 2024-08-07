from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Import serializers and models
from .serializer import *
from .models import *
from .ai_module import generate_financial_report

# Create your views here.

@login_required
def generate_report_view(request):
    """
    Generate a financial report for the logged-in user and save it to the database.
    Returns a JSON response containing the newly created report.
    """
    user = request.user
    report_text = generate_financial_report(user)
    report = FinancialReport.objects.create(
        user=user,
        report_name="AI Generated Report",
        report_data={'summary': report_text}
    )
    # Serialize the created report for the response
    serializer = FinancialReportSerializer(report)
    return JsonResponse(serializer.data, status=200)

class ExpenseCategoryListView(generics.ListAPIView):
    """
    List all ExpenseCategory instances for the specified user.
    """
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter ExpenseCategory instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return ExpenseCategory.objects.filter(user_id=user_id)

class TransactionListView(generics.ListAPIView):
    """
    List all Transaction instances for the specified user.
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter Transaction instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return Transaction.objects.filter(user_id=user_id)

class BudgetListView(generics.ListAPIView):
    """
    List all Budget instances for the specified user.
    """
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter Budget instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return Budget.objects.filter(user_id=user_id)

class FinancialGoalListView(generics.ListAPIView):
    """
    List all FinancialGoal instances for the specified user.
    """
    serializer_class = FinancialGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter FinancialGoal instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return FinancialGoal.objects.filter(user_id=user_id)


#? Notification

class NotificationListView(generics.ListAPIView):
    """
    List all Notification instances for the specified user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter Notification instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return Notification.objects.filter(user_id=user_id)
    
class NotificationListUnreadView(generics.ListAPIView):
    """
    List all Notification instances for the specified user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter Notification instances by the user specified in the URL parameter 
        and filter unread Notification.
        """
        user_id = self.kwargs.get('user_id')
        return Notification.objects.filter(user_id=user_id).exclude(is_read=True)

class UpdateListView(generics.ListAPIView):
    """
    List all Update instances for the specified user.
    """
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter Update instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return Update.objects.filter(user_id=user_id)

class FinancialAnalyticsListView(generics.ListAPIView):
    """
    List all FinancialAnalytics instances for the specified user.
    """
    serializer_class = FinancialAnalyticsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter FinancialAnalytics instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return FinancialAnalytics.objects.filter(user_id=user_id)

class FinancialReportListView(generics.ListAPIView):
    """
    List all FinancialReport instances for the specified user.
    """
    serializer_class = FinancialReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter FinancialReport instances by the user specified in the URL parameter.
        """
        user_id = self.kwargs.get('user_id')
        return FinancialReport.objects.filter(user_id=user_id)
