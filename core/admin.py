from django.contrib import admin
from .models import NotificationPreference, NotificationType


@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    """Admin for Notification Preference"""
    list_display = ('noti_type', 'is_email', 'is_mobile', 'is_sms')


@admin.register(NotificationType)
class NotificationTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'frequency')
