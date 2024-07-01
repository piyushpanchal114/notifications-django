from django.urls import path
from . import views


urlpatterns = [
    path("notifications/",
         views.NotificationPreferenceRetrieveUpdateAPIView.as_view()),
    path("notifications/<int:pk>/preferences/",
         views.NotificationTypeRetrieveUpdateAPIView.as_view())
]
