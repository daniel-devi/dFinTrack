from celery import shared_task
from django.utils import timezone
from .models import *

#? Budget

# Task to check Budget End Date and determine if Valid or not
@shared_task
def check_budget_end_dates():
    today = timezone.now().date()
    budgets = Budget.objects.filter(end_date=today)
    for budget in budgets:
        # Perform actions when the end_date is today
        # Variables
        user = budget.user
        NOTIFICATION_TYPE = ('budget_deadline', 'Budget End Date Reached')
        MESSAGE = f"Budget '{budget.name.upper()}' has reached its end date today."
        # - Notify users
        Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE)
        # - Update the budget status to not valid
        budget.valid = False