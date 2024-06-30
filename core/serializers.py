from rest_framework import serializers
from .models import NotificationPreference, NotificationType


class NotificationPreferenceSerializer(serializers.ModelSerializer):
    """Serializer for Notification Preference"""
    class Meta:
        model = NotificationPreference
        fields = ('is_email', 'is_mobile', 'is_sms')
        extra_kwargs = {
            'is_email': {'required': True},
            'is_mobile': {'required': True},
            'is_sms': {'required': True}}

    def update(self, instance, validated_data):
        is_email = validated_data.get("is_email")
        is_mobile = validated_data.get("is_mobile")
        is_sms = validated_data.get("is_sms")

        instance.is_email = is_email
        instance.is_mobile = is_mobile
        instance.is_sms = is_sms
        instance.save()
        return instance


class NotificationTypeSerializer(serializers.ModelSerializer):
    """Serializer for Notification Type"""
    preference = NotificationPreferenceSerializer()

    class Meta:
        model = NotificationType
        fields = ('preference', 'type', 'frequency')
