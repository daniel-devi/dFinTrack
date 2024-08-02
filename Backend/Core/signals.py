from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
# Core
from .models import *
# Accounts
from Accounts.models import Account


#* Create Signals for Core Models


#? Transaction Model 

# Update User Account on Transaction Model Change
@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, **kwargs):
    account = instance.account # Get the User Account
    if instance.transaction_type in ['debit', 'purchase']:
        # For debits and purchases, subtract the amount from the balance
        account.balance -= instance.amount
    elif instance.transaction_type in ['credit', 'refund']:
        # For credits and refunds, add the amount to the balance
        account.balance += instance.amount
    else:
        # Handle unexpected transaction types
        account.balance = account.balance
    
    account.save()
    


#? Budget

# Update Budget Valid Field
@receiver(post_save, sender=Budget)
def check_end_date(sender, instance, **kwargs):
    if instance.end_date == timezone.now().date():
        # when end_date matches current date valid field is equal to false
        instance.valid = False
    else:
        # Reschedule the signal to run again the next day
        next_check = timezone.now() + timedelta(days=1)
        instance.end_date = next_check
        instance.save()


# Update User Budget Amount_Spent on Transaction Model Change
@receiver(post_save, sender=Transaction)
def update_budget_account_spent(sender, instance, **kwargs):
    user = instance.user # Get the User Account
    budget = Budget.objects.filter(user=user).filter(valid=True) # Gets User Budget that is active
    budget_account = budget.amount # get amount left for Budget
    budget_account_left = budget.amount_left # get amount left for Budget
    
    if instance.category == budget.category and instance.value == True:
        if instance.transaction_type in ['debit', 'purchase']:
            # For debits and purchases, subtract the amount from the balance
            budget_account_left -= instance.amount
        elif instance.transaction_type in ['credit', 'refund']:
            # For credits and refunds, add the amount to the balance
            budget_account += instance.amount
        else:
            # Handle unexpected transaction types
            budget_account = budget_account
    
    instance.save()
    