from django.conf.urls import url
from django.urls import include, re_path, path
from django.conf import settings

urlpatterns_debug = []

if settings.DEBUG:
    import debug_toolbar

    urlpatterns_debug += [
        path(r'__debug__/', include(debug_toolbar.urls)),
        re_path(r'^silk/', include('silk.urls', namespace='silk'))
    ]
