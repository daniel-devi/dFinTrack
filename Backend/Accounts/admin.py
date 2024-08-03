from django.contrib import admin
from .models import *

#* Register your models here.

# PaymentCardDetail PaymentCardDetailAdmin
@admin.register(PaymentCardDetail)
class PaymentCardDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'cardholder_name', 'created_at')
    search_fields = ('user__username', 'cardholder_name')
    readonly_fields = ('encrypted_card_number', 'encrypted_expiry_date', 'encrypted_cvv')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields

# Account AccountAdmin
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'balance', "currency")
    search_fields = ('user__username', 'account_type', "currency", "created_at")
    list_filter = ('account_type', "currency", "created_at")
    readonly_fields = ("created_at", "updated_at")

# UserProfile UserProfileAdmin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user_username',)
    readonly_fields = ('profile_picture',)  # Optionally make the profile picture field read-only
    