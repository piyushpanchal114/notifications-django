from rest_framework import serializers
from .models import NotificationPreference, NotificationType


class NotificationPreferenceSerializer(serializers.ModelSerializer):
    """Serializer for Notification Preference"""
    class Meta:
        model = NotificationPreference
        fields = ('is_email', 'is_mobile', 'is_sms')


class NotificationTypeSerializer(serializers.ModelSerializer):
    """Serializer for Notification Type"""
    preference = NotificationPreferenceSerializer()

    class Meta:
        model = NotificationType
        fields = ('preference', 'type', 'frequency')
