from django.urls import path
# Core
from .views import * 

# "localhost/Core-api" Views List 
# All the endpoints for the URl

urlpatterns = [
    # Endpoint to retrieve a list of all Notification that belongs. only the user
    path('Notification/get-user-notification-unread/<int:user_id>/', NotificationListUnreadView.as_view(), name='user-list-by-username'),
]