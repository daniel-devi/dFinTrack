from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import pandas as pd
from datetime import date
from transformers import pipeline
import datetime
from .models import Transaction, Budget, FinancialGoal, FinancialReport
from .serializer import FinancialReportSerializer
from Accounts.models import Account
import tensorflow as tf
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Ai View
class FinancialReportView(APIView):
    """
    API view to generate and return a financial report for a user.
    """
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_transaction_data(self, user):
        """
        Retrieve transaction data for the given user from the database and return it as a DataFrame.
        """
        transactions = Transaction.objects.filter(user=user).values()  # Get transactions for the user
        if transactions.exists():
            return pd.DataFrame(transactions)  # Convert to DataFrame

    def generate_insights(self, data, user):
        """
        Generate financial insights based on transaction data and user-specific information such as budget and financial goals.
        """
        insights = {}
        budget = Budget.objects.filter(user=user).first()  # Get the user's active budget
        financial_goals = FinancialGoal.objects.filter(user=user, completed=False)  # Get the user's incomplete financial goals

        # Calculate total income and expenses
        if data is not None:  # Checks if there is Data before does action
            total_income = data[data['transaction_type'].isin(['credit', 'refund'])]['amount'].sum()
            total_expenses = data[data['transaction_type'].isin(['debit', 'purchase'])]['amount'].sum()
            insights['total_income'] = total_income
            insights['total_expenses'] = total_expenses
            insights['net_balance'] = total_income - total_expenses

            # Calculate monthly expenses by category
            data['timestamp'] = pd.to_datetime(data['timestamp'])
            data.set_index('timestamp', inplace=True)

            # Group by month and category, then calculate the sum efficiently
            monthly_expenses = data.groupby([pd.Grouper(freq='ME'), 'category_id'])['amount'].sum()

            # Convert to dictionary with fill value of 0 for missing categories
            insights['monthly_expenses_by_category'] = monthly_expenses.unstack(fill_value=0).to_dict()

            # Determine budget adherence
            if budget is not None:
                current_date = date.today()
                if current_date <= budget.end_date:
                    if total_expenses <= budget.amount:
                        insights['budget_status'] = f"You are within your budget of {budget.amount}."
                    else:
                        insights['budget_status'] = f"You have exceeded your budget of {budget.amount}."
                else:
                    insights['budget_status'] = "Your budget period has ended."
            else:
                insights['budget_status'] = "No active budget found."

            # Track financial goals progress
            goal_progress = {}
            for goal in financial_goals:
                goal_progress[goal.name] = {
                    'target_amount': goal.target_amount,
                    'current_amount': goal.current_amount,
                    'remaining_amount': goal.target_amount - goal.current_amount,
                    'progress': (goal.current_amount / goal.target_amount) * 100 if goal.target_amount > 0 else 0
                }
            insights['goal_progress'] = goal_progress

        return insights

    def generate_spending_suggestions(self, insights, budget):
        """
        Generate suggestions for spending adjustments to stay within budget based on current insights.
        """
        suggestions = []
        if 'monthly_expenses_by_category' in insights:
            for month, categories in insights['monthly_expenses_by_category'].items():
                for category, amount in categories.items():
                    if amount is not None:
                        if amount > (budget.amount / len(categories)):  # Check if spending exceeds a simple threshold
                            suggestions.append(f"Consider reducing spending in {category} for {month} to stay within budget.")
                        else:
                            suggestions.append(f"Spending in {category} for {month} is within budget.")

        return suggestions

    def generate_nlp_report(self, insights, suggestions):
        """
        Generate a natural language summary report based on the financial insights using a summarization model.
        """
        summarizer = pipeline('summarization', model="t5-base", tokenizer="t5-base", framework="tf")
        report_text = f"Total income: {insights['total_income']}, Total expenses: {insights['total_expenses']}, Net balance: {insights['net_balance']}."
        
        if 'budget_status' in insights:
            report_text += f" Budget status: {insights['budget_status']}."
        
        if 'goal_progress' in insights:
            for goal, progress in insights['goal_progress'].items():
                report_text += f" Goal {goal}: {progress['progress']}% complete with {progress['remaining_amount']} remaining to reach {progress['target_amount']}."
        
        report_text += " Suggestions for spending adjustments: " + " ".join(suggestions)
        
        try:
            summary = summarizer(report_text, max_length=200, min_length=50, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error generating summary: {str(e)}"

    def post(self, request):
        """
        Handle POST requests to generate and return the financial report.
        """
        user = request.user  # Get the authenticated user
        account = Account.objects.filter(user=user).first()
        data = self.get_transaction_data(user)  # Retrieve transaction data
        print("", data, "#############")
        insights = self.generate_insights(data, user)  # Generate insights
        budget = Budget.objects.filter(user=user).first()  # Re-fetch the budget to ensure it's available
        suggestions = self.generate_spending_suggestions(insights, budget)  # Generate spending suggestions
        report_text = self.generate_nlp_report(insights, suggestions)  # Generate NLP report text
        
        # Structure the response data
        generated_report_data = {
            'total_income': insights['total_income'],
            'total_expenses': insights['total_expenses'],
            'net_balance': insights['net_balance'],
            'budget_status': insights.get('budget_status', ''),
            'goal_progress': insights['goal_progress'],
            'suggestions': suggestions,
            'report_text': report_text,
            'insights': insights  # Including raw insights data for detailed analysis
        }

        # Create a new FinancialReport object
        report = {
            "user":user,
            "account":account,
            "report_name": f"Financial Report at {datetime.datetime.now()}",
            "report_data": generated_report_data,
        }
            
        FinancialReport.objects.create(
            user=user,
            account=account,
            report_name=f"Financial Report at {datetime.datetime.now()}",
            report_data=generated_report_data,
        )
        
        # Serialize and return the response data as JSON
        serializer = FinancialReportSerializer(report)
        return Response(serializer.data, status=201)
