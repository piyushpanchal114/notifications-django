from rest_framework.generics import RetrieveUpdateAPIView
from .models import NotificationType, NotificationPreference
from .serializers import (NotificationPreferenceSerializer,
                          NotificationTypeSerializer)


class NotificationPreferenceRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """View for updating Notification Preferences"""
    serializer_class = NotificationPreferenceSerializer

    def get_object(self):
        return NotificationPreference.objects.filter(
            user=self.request.user).last()


class NotificationTypeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """View for retrieving the notification preference"""
    serializer_class = NotificationTypeSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return NotificationType.objects.filter(
            user=self.request.user)
