from rest_framework import serializers
from .models import NotificationType, NotificationPreference


class NotificationPreferenceSerializer(serializers.Serializer):
    """Serializer for Notification Preference"""
    is_email = serializers.BooleanField()
    is_mobile = serializers.BooleanField()
    is_sms = serializers.BooleanField()

    def update(self, instance, validated_data):
        is_email_data = validated_data["is_email"]
        is_mobile_data = validated_data["is_mobile"]
        is_sms_data = validated_data["is_sms"]
        if is_email_data is not None and not is_email_data:
            NotificationPreference.objects\
                .filter(noti_type__user=self.context["user"])\
                .update(is_email=is_email_data)
        if is_mobile_data is not None and not is_mobile_data:
            NotificationPreference.objects\
                .filter(noti_type__user=self.context["user"])\
                .update(is_mobile=is_mobile_data)
        if is_sms_data is not None and not is_sms_data:
            NotificationPreference.objects\
                .filter(noti_type__user=self.context["user"])\
                .update(is_sms=is_sms_data)
        return instance


class NotificationTypeSerializer(serializers.ModelSerializer):
    """Serializer for Notification Type"""
    noti_prefs = NotificationPreferenceSerializer()

    class Meta:
        model = NotificationType
        fields = ('id', 'type', 'frequency', 'noti_prefs')


class NotificationTypeListSerializer(serializers.ListSerializer):
    """List Serializer for Notification"""

    def update(self, instance, validated_data):
        noti_type_mapping = {n.id: n for n in instance}
        data_mapping = {item['id']: item for item in validated_data}

        ret = []
        for noti_type_id, data in data_mapping.items():
            noti_type = noti_type_mapping.get(noti_type_id, None)
            if noti_type is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(noti_type, data))
        return ret


class NotificationTypeUpdateSerializer(serializers.ModelSerializer):
    """Serializer for Notification Type"""
    id = serializers.IntegerField()
    noti_prefs = NotificationPreferenceSerializer()

    class Meta:
        model = NotificationType
        fields = ('id', 'frequency', 'noti_prefs')
        list_serializer_class = NotificationTypeListSerializer

    def update(self, instance, validated_data):
        instance.frequency = validated_data.get(
            'frequency', instance.frequency)
        instance.save()

        noti_prefs = validated_data.get('noti_prefs')

        for pref in noti_prefs:
            if pref:
                instance.noti_prefs.is_email = noti_prefs.get(
                    'is_email', instance.noti_prefs.is_email)
                instance.noti_prefs.is_mobile = noti_prefs.get(
                    'is_mobile', instance.noti_prefs.is_mobile)
                instance.noti_prefs.is_sms = noti_prefs.get(
                    'is_sms', instance.noti_prefs.is_sms)
                instance.noti_prefs.save()

        return instance
