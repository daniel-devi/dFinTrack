import pandas as pd
from datetime import date
from .models import Transaction, Budget, FinancialGoal, FinancialReport, FinancialAnalytics
from transformers import pipeline

def get_transaction_data(user):
    transactions = Transaction.objects.filter(user=user).values()
    return pd.DataFrame(transactions)

def generate_insights(data, user):
    insights = {}
    budget = Budget.objects.filter(user=user)
    financial_goals = FinancialGoal.objects.filter(user=user).exclude(completed=True)

    total_income = data[data['transaction_type'].isin(['credit', 'refund'])]['amount'].sum()
    total_expenses = data[data['transaction_type'].isin(['debit', 'purchase'])]['amount'].sum()

    insights['total_income'] = total_income
    insights['total_expenses'] = total_expenses
    insights['net_balance'] = total_income - total_expenses

    # Spending trends and patterns
    insights['monthly_expenses'] = data.set_index('timestamp').resample('M')['amount'].sum().to_dict()

    # Check budget adherence
    if budget:
        current_date = date.today()
        if current_date <= budget.end_date:
            insights['budget_status'] = f"You are within your budget of {budget.amount}" if total_expenses <= budget.amount else f"You have exceeded your budget of {budget.amount}"
        else:
            insights['budget_status'] = "Your budget period has ended."

    # Financial goals progress
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

def generate_nlp_report(insights):
    summarizer = pipeline('summarization')
    report_text = f"Total income: {insights['total_income']}, Total expenses: {insights['total_expenses']}, Net balance: {insights['net_balance']}."
    if 'budget_status' in insights:
        report_text += f" Budget status: {insights['budget_status']}."
    if 'goal_progress' in insights:
        for goal, progress in insights['goal_progress'].items():
            report_text += f" Goal {goal}: {progress['progress']}% complete with {progress['remaining_amount']} remaining to reach {progress['target_amount']}."
    summary = summarizer(report_text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def generate_financial_report(user):
    data = get_transaction_data(user)
    insights = generate_insights(data, user)
    report_text = generate_nlp_report(insights)
    return report_text
