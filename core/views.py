from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from .models import NotificationType
from .serializers import (NotificationPreferenceSerializer,
                          NotificationTypeSerializer)


class NotificationTypeRetrieveAPIView(RetrieveUpdateAPIView):
    """View for retrieving the notification preference"""
    serializer_class = NotificationTypeSerializer

    def get_object(self):
        return NotificationType.objects.filter(
            preference__user=self.request.user).first()
