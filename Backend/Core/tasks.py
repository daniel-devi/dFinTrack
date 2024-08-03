from celery import shared_task
from django.utils import timezone
import datetime
# Core
from .models import *

#? Budget

# Task to check Budget End Date and determine if Valid or not
@shared_task
def check_budget_end_dates():
    NOTIFICATION_TYPE = 'budget_deadline', 'Budget End Date Reached'
    MESSAGE = f"Budget '{budget.name.upper()}' created by {budget.user.first_name} {budget.user.last_name} 
    on {budget.created_at} has reached its end date today."
    today = timezone.now().date()
    budgets = Budget.objects.filter(end_date=today).filter(valid=True)
    for budget in budgets:
        # Perform actions when the end_date is today
        # Variables
        user = budget.user
        
        # - Notify users
        Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE)
        # - Update the budget status to not valid
        budget.valid = False
    
    budget.save()
        
    
def check_budget_has_been_exceeded():
    NOTIFICATION_TYPE = 'budget_exceed', 'Budget Limit has been Exceeded'
    MESSAGE = f"Budget '{budget.name.upper()}' created by {budget.user.first_name} {budget.user.last_name} on 
            {budget.created_at} has been reached exceeded although it ends on {budget.end_date}.
            \nThe Budget is {budget.amount} as of {budget.updated_at}- the spending is exceeded by {over_budget} "
    today = datetime.datetime.now()
    budgets = Budget.objects.filter(valid=True).exclude(end_date=today)
    for budget in budgets:
        # Perform actions when the target has been reached
        # Variables
        user = budget.user
        over_budget = budget.amount - budget.amount_spent
        
        # Check if user target has been reached
        if budget.amount_spent > budget.current_amount:            
            # - Notify users
            Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE)
            # - Update the financial_goal status to not valid and completed True
            budget.exceeded = True
        
    budget.save()

#? Financial Goal

# Task to check Financial Goal End Date and determine if Valid or not
@shared_task
def check_financial_goal_end_dates():
    financial_goal = FinancialGoal.objects.filter(end_date=today).filter(valid=True)
    for goals in financial_goal:
        # Perform actions when the end_date is today
        #* Variables 
        # # Adds the number of days from current date
        today = timezone.now().date()
        user = goals.user
        NOTIFICATION_TYPE =  'financial_goal_deadline', 'You have Reached the end date of your Financial Goal'
        MESSAGE = f"Financial Goal '{goals.name.upper()}' created by {goals.user.first_name} {goals.user.last_name} on 
            {goals.created_at} has reached its end date today {goals.target_date}."
        # - Notify users
        Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE)
        # - Update the financial_goal status to not valid
        goals.valid = False
        
        goals.save()
  
        
        
# Task to check Financial Goal End date and give reminders at different intervals (7days, 3days, a day)
@shared_task
def check_financial_goal_end_dates_and_sends_reminder():
    financial_goal = FinancialGoal.objects.filter(valid=True)
    for goals in financial_goal:
        # Perform actions when the end_date is today
        #* Variables 
        # # Adds the number of days from current date
        today = timezone.now().date()
        a_week_from_today = today + timezone.timedelta(days=7)
        three_days_from_today = today + timezone.timedelta(days=3)
        a_days_from_today = today + timezone.timedelta(days=1)
        user = goals.user
        NOTIFICATION_TYPE =  f"financial_goal_deadline',
        'Just a reminder that your Financial Goal: {goals.name}-{goals.goal_type} ends on {goals.target_date}"
        #* Messages for different Dates  
        MESSAGE_A_WEEK = f"Financial Goal '{goals.name.upper()}' created by {goals.user.first_name} {goals.user.last_name} on 
            {goals.created_at} will reach its end date by {goals.target_date} that is a week from Today."
        MESSAGE_THREE_DAYS = f"Financial Goal '{goals.name.upper()}' created by {goals.user.first_name} {goals.user.last_name} on 
            {goals.created_at} will reach its end date by {goals.target_date} that is three days from Today."
        MESSAGE_A_DAYS = f"Financial Goal '{goals.name.upper()}' created by {goals.user.first_name} {goals.user.last_name} on 
            {goals.created_at} will reach its end date by {goals.target_date} that is a days from Today."
        # - Notify users
        if goals.target_date == a_week_from_today:
            Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE_A_WEEK)
        elif goals.target_date == three_days_from_today:
            Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE_THREE_DAYS)
        elif goals.target_date == a_days_from_today:
            Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE_A_DAYS)
            


# Task to check Financial Goal has reached it's target Goal and determine if Valid or not
@shared_task
def check_financial_goals_has_been_met():
    NOTIFICATION_TYPE =  'financial_goal_reached', 'You have Reached your Financial Goal congratulation🎉'
    MESSAGE = f"Financial Goal '{goals.name.upper()}' created by {goals.user.first_name} {goals.user.last_name} on 
            {goals.created_at} has been reached {today}."
    financial_goal = FinancialGoal.objects.filter(valid=True).filter(completed=False)
    today = datetime.datetime.now()
    for goals in financial_goal:
        # Perform actions when the target has been reached
        # Variables
        user = goals.user
       
        # Check if user target has been reached
        if goals.target_amount == goals.current_amount:            
            # - Notify users
            Notification.objects.create(user=user, notification_type=NOTIFICATION_TYPE, message=MESSAGE)
            # - Update the financial_goal status to not valid and completed True
            goals.valid = False
            goals.completed = True 
        
        goals.save()