from rest_framework.generics import RetrieveUpdateAPIView
from .models import NotificationType, NotificationPreference
from .serializers import (NotificationPreferenceSerializer,
                          NotificationTypeSerializer)


class NotificationPreferenceRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """View for updating Notification Preferences"""
    serializer_class = NotificationPreferenceSerializer
    http_method_names = ["get", "put", "options"]

    def get_object(self):
        return NotificationPreference.objects.filter(
            user=self.request.user).first()


class NotificationTypeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """View for retrieving the notification preference"""
    serializer_class = NotificationTypeSerializer

    def get_object(self):
        return NotificationType.objects.filter(
            preference__user=self.request.user).first()
