from rest_framework import serializers
from .models import NotificationPreference, NotificationType


class NotificationPreferenceSerializer(serializers.ModelSerializer):
    """Serializer for Notification Preference"""
    class Meta:
        model = NotificationPreference
        fields = ('is_email', 'is_mobile', 'is_sms')

    def update(self, instance, validated_data):
        is_email = validated_data.get("is_email")
        is_mobile = validated_data.get("is_mobile")
        is_sms = validated_data.get("is_sms")

        if is_email is not None:
            instance.is_email = is_email
            instance.user.noti_types.all().update(is_email=is_email)
        if is_mobile is not None:
            instance.is_mobile = is_mobile
            instance.user.noti_types.all().update(is_mobile=is_mobile)
        if is_sms is not None:
            instance.is_sms = is_sms
            instance.user.noti_types.all().update(is_sms=is_sms)
        instance.save()
        return instance


class NotificationTypeSerializer(serializers.ModelSerializer):
    """Serializer for Notification Type"""
    class Meta:
        model = NotificationType
        fields = ('id', 'type', 'frequency', 'is_email',
                  'is_mobile', 'is_sms')

    def update(self, instance, validated_data):
        type = validated_data.get("type")
        frequency = validated_data.get("frequency")
        is_email = validated_data.get("is_email")
        is_mobile = validated_data.get("is_mobile")
        is_sms = validated_data.get("is_sms")
        if type:
            instance.type = type
        if frequency:
            instance.frequency = frequency
        if is_email is not None:
            instance.is_email = is_email
        if is_mobile is not None:
            instance.is_mobile = is_mobile
        if is_sms is not None:
            instance.is_sms = is_sms
        instance.save()
        return instance
