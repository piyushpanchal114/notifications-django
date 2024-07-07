from django.urls import path
from . import views


urlpatterns = [
    path("notifications/",
         views.NotificationBulkListUpdateView.as_view()),
    path("preferences/",
         views.NotificationPreferenceAPIView.as_view())
]
