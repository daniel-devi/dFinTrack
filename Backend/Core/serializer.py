from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from Accounts.models import Account

# Serializer for ExpenseCategory model
class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'  # Serialize all fields

    def validate_category_type(self, value):
        """Ensure the category type is valid."""
        if value not in dict(ExpenseCategory.CATEGORY_TYPES).keys():
            raise serializers.ValidationError("Invalid category type.")
        return value


# Serializer for Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # Serialize all fields

    def validate_currency(self, value):
        """Ensure the currency is valid."""
        if value not in dict(Transaction.CURRENCY_CHOICES).keys():
            raise serializers.ValidationError("Invalid currency.")
        return value


# Serializer for Budget model
class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'  # Serialize all fields

    def validate(self, data):
        """Ensure that end_date is after start_date."""
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data


# Serializer for FinancialGoal model
class FinancialGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialGoal
        fields = '__all__'  # Serialize all fields

    def validate(self, data):
        """Ensure that target_date is after start_date."""
        if data['target_date'] < data['start_date']:
            raise serializers.ValidationError("Target date must be after start date.")
        return data


# Serializer for Notification model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'  # Serialize all fields


# Serializer for Update model
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'  # Serialize all fields


# Serializer for FinancialAnalytics model
class FinancialAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAnalytics
        fields = '__all__'  # Serialize all fields

    def update_analytics(self):
        """Update financial analytics based on related transactions."""
        transactions = Transaction.objects.filter(account=self.account, user=self.user)
        self.total_income = sum(t.amount for t in transactions if t.transaction_type in ['credit', 'refund'])
        self.total_expenses = sum(t.amount for t in transactions if t.transaction_type in ['debit', 'purchase'])
        self.net_balance = self.total_income - self.total_expenses
        self.save()


# Serializer for FinancialReport model
class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'  # Serialize all fields

    def generate_report(self):
        """Generate and save the financial report data."""
        analytics = FinancialAnalytics.objects.filter(account=self.account, user=self.user).latest('report_date')
        self.report_data = {
            'total_income': str(analytics.total_income),
            'total_expenses': str(analytics.total_expenses),
            'net_balance': str(analytics.net_balance),
            'report_date': analytics.report_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.save()
