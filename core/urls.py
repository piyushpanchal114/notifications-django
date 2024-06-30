from django.urls import path
from . import views


urlpatterns = [
    path("preferences/",
         views.NotificationPreferenceRetrieveAPIView.as_view())
]
