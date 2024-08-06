from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Accounts
from .models import *

#* Creates Signal for Accounts Models


#? UserProfile 

# Create a UserProfile Model object linked to created User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Updates Model object on Save if Model has a related User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'): # This checks if the User instance has a related UserProfile
        instance.userProfile.save()


#? Signal for Creating an Account on User MODEL CREATION
# Create a Account Model object linked to created User
@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, account_type="current" )
# Updates Model object on Save if Model has a related User
@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    if hasattr(instance, 'account'):  # This checks if the User instance has a related Account
        instance.account.save()
