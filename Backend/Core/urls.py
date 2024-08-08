from django.urls import path
# Core
from .views import * 
from .ai_module import FinancialReportView

# "localhost/Core-api" Views List 
# All the endpoints for the URl

urlpatterns = [
    # Endpoint to retrieve a list of all Notification that belongs. only the user
    path('Notification/get-user-notification-unread/<int:user_id>/', NotificationListUnreadView.as_view(), name='user-list-by-username'),
    # Route for financial report API
    path('Financial-report/generate-report', FinancialReportView.as_view(), name='financial-report'), 
    # URL pattern for listing expense categories by user_id
    path('Expense-Category/get-categories/<int:user_id>/', ExpenseCategoryNameListView.as_view(), name='expense-category-list'), 
    # URL For Transaction Type Account
    path("Transaction/get-type", TransactionTypeView.as_view(), name="transaction-type"),
]

