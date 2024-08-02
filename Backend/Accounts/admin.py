from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'balance', "currency")
    search_fields = ('user__username', 'account_type', "currency", "created_at")
    list_filter = ('account_type', "currency", "created_at")
    readonly_fields = ("created_at", "updated_at")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user_username',)
    readonly_fields = ('profile_picture',)  # Optionally make the profile picture field read-only
    