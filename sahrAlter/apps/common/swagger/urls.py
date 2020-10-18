from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import xadmin
import notifications.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Geek Form",
        default_version='v1',
        description="description",
        terms_of_service="https://localhost",
        contact=openapi.Contact(email="contact@localhost.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns_swagger = [

    url(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/docs/', include_docs_urls(title="API文档")),

]
