from django.db.models import Q, Count
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from .models import NotificationType, NotificationPreference
from .serializers import (NotificationTypeUpdateSerializer,
                          NotificationTypeSerializer,
                          NotificationPreferenceSerializer,
                          NotificationTypeListSerializer)


class NotificationPreferenceAPIView(GenericAPIView):
    """View for retrieving the notification preference"""
    serializer_class = NotificationPreferenceSerializer

    def get(self, request):
        qs = NotificationPreference.objects.filter(
            noti_type__user=request.user).aggregate(
                email=Count("is_email", filter=Q(is_email=True)),
                mobile=Count("is_mobile", filter=Q(is_mobile=True)),
                sms=Count("is_sms", filter=Q(is_sms=True)))
        res = {"is_email": True, "is_mobile": True, "is_sms": True}
        if qs["email"] == 0:
            res["is_email"] = False
        if qs["mobile"] == 0:
            res["is_mobile"] = False
        if qs["sms"] == 0:
            res["is_sms"] = False
        response = self.serializer_class(res)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = NotificationPreference.objects.filter(
            noti_type__user=request.user).first()
        serializer = NotificationPreferenceSerializer(
            instance, data=request.data, partial=False,
            context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = request.data
        return Response(data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()


class NotificationBulkListUpdateView(ListAPIView):
    """
    List/Update the relationships between Labels and CaptureSamples
    """

    serializer_class = NotificationTypeSerializer

    def get_queryset(self):
        return NotificationType.objects.filter(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = NotificationTypeListSerializer(
            instances, data=request.data, partial=False,
            child=NotificationTypeUpdateSerializer())
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()
