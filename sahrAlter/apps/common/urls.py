from django.urls import include, re_path

from .notification.urls import urlpatterns_notification
from .jwt.urls import urlpatterns_jwt
from .swagger.urls import urlpatterns_swagger
from .debug.urls import urlpatterns_debug

urlpatterns_common = []
urlpatterns_common += urlpatterns_jwt
urlpatterns_common += urlpatterns_swagger
urlpatterns_common += urlpatterns_notification
urlpatterns_common += urlpatterns_debug
