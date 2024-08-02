from django.contrib import admin
from .models import *

#* Register your models here.

# ExpenseCategory ModelAdmin
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category_type', 'created_at', 'updated_at')
    
 
# Budget ModelAdmin
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'amount', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name', 'user__username')
    list_filter = ('category', 'start_date', 'end_date', 'created_at', 'updated_at')
    
    
# Transaction ModelAdmin
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'transaction_type', 'status', 'currency', 'amount', 'transaction_uid', 'category', 'description', 'timestamp')
    search_fields = ('user__username', 'account__name', 'transaction_uid', 'description')
    list_filter = ('transaction_type', 'status', 'currency', 'timestamp')
    
    
# FinancialGoal ModelAdmin
@admin.register(FinancialGoal)
class FinancialGoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'goal_type', 'target_amount', 'current_amount', 'start_date', 'target_date', 'created_at', 'updated_at')
    search_fields = ('name', 'goal_type', 'user__username')
    list_filter = ('goal_type', 'start_date', 'target_date', 'created_at', 'updated_at')
    
    
# Notification ModelAdmin
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read')
    search_fields = ('message',)
    

# Update ModelAdmin
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('user', 'update_type', 'created_at')
    list_filter = ('update_type',)
    search_fields = ('message',)
    
