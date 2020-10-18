from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import (NotificationViewSet)

router = routers.DefaultRouter()

router.register(r'', NotificationViewSet, base_name="notification")

urlpatterns_notification = [
    url(r'^api/notification/', include(router.urls)),
]
