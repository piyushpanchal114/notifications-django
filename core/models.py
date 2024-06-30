from django.db import models
from django.contrib.auth.models import User


class NotificationPreference(models.Model):
    """Model for Notification Preference"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_email = models.BooleanField(default=True)
    is_mobile = models.BooleanField(default=True)
    is_sms = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.first_name


class NotificationType(models.Model):
    """Model for Notification Type"""
    FREQUENCY_CHOICES = [
        ("p", "Periodically"),
        ("i", "Instantly"),
        ("r", "rarely")
    ]

    preference = models.ForeignKey(
        NotificationPreference, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    frequency = models.CharField(
        max_length=5, choices=FREQUENCY_CHOICES, default="p")

    def __str__(self) -> str:
        return self.preference_type

    class Meta:
        unique_together = ("preference", "type")
