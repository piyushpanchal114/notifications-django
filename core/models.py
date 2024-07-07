from django.db import models
from django.contrib.auth.models import User


class NotificationType(models.Model):
    """Model for Notification Type"""
    FREQUENCY_CHOICES = [
        ("p", "Periodically"),
        ("i", "Instantly"),
        ("r", "rarely")
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="noti_types")
    type = models.CharField(max_length=255, unique=True)
    frequency = models.CharField(
        max_length=5, choices=FREQUENCY_CHOICES, default="p")

    def __str__(self) -> str:
        return self.type


class NotificationPreference(models.Model):
    """Model for Notification Preference"""
    noti_type = models.OneToOneField(
        NotificationType, on_delete=models.CASCADE, related_name="noti_prefs")
    is_email = models.BooleanField(default=True)
    is_mobile = models.BooleanField(default=True)
    is_sms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.noti_type}"
