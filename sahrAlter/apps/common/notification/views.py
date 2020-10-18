from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import include, re_path, path, NoReverseMatch
from notifications.views import \
    live_all_notification_count, \
    live_all_notification_list, \
    live_unread_notification_count, \
    live_unread_notification_list, delete, mark_all_as_read, mark_as_read, mark_as_unread
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.serializers import BaseSerializer


def HttpResponseToJsonResponse(res):
    print(res)
    return res


class NotificationSlugSerializer(serializers.ModelSerializer):
    slug = serializers.Field()

    class Meta:
        fields = ('slug',)


# TODO: 调用view函数有问题

class NotificationViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.DestroyModelMixin):
    "提醒"

    serializer_class = (NotificationSlugSerializer,)

    def list(self, request, *args, **kwargs):
        """获取所有提醒"""
        return live_all_notification_list(request)

    def destroy(self, request, *args, **kwargs):
        """删除提醒"""

        try:
            delete(request, slug=kwargs["pk"])
        except NoReverseMatch:
            return JsonResponse({"status": "ok"})

    @action(detail=False, methods=["get"])
    def count(self, request):
        """获取所有提醒数量"""
        return live_all_notification_count(request)

    @action(detail=False, methods=["get"])
    def unread(self, request):
        """获取未读提醒"""
        return live_unread_notification_list(request)

    @action(detail=False, methods=["get"])
    def unread_count(self, request):
        """获取未读数量"""
        return live_unread_notification_count(request)

    @action(detail=True, methods=["patch"])
    def mark_as_read(self, request, *args, **kwargs):
        """设置已读"""
        try:
            mark_as_read(request, slug=kwargs["pk"])
        except NoReverseMatch:
            return JsonResponse({"status": "ok"})

    @action(detail=True, methods=["patch"])
    def mark_as_unread(self, request, *args, **kwargs):
        """设置未读"""
        try:
            mark_as_unread(request, slug=kwargs["pk"])
        except NoReverseMatch:
            return JsonResponse({"status": "ok"})

    @action(detail=False, methods=["delete"])
    def delete_all_read(self, request, *args, **kwargs):
        """删除所有已读"""

        # return JsonResponse({"status": "ok"})

#
# re_path(r'^api/notification/mark-all-as-read/$', mark_all_as_read, name='mark_all_as_read'),
#     re_path(r'^api/notification/mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),
#     re_path(r'^api/notification/mark-as-unread/(?P<slug>\d+)/$', mark_as_unread, name='mark_as_unread'),
#     re_path(r'^api/notification/delete/(?P<slug>\d+)/$', delete, name='delete'),
#
