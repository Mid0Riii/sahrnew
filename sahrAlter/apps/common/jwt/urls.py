from django.conf.urls import url
from rest_framework_jwt.serializers import JSONWebTokenSerializer, VerifyJSONWebTokenSerializer, \
    RefreshJSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView


# 重写方法描述

class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    使用帐号密码获取JWT
    """
    serializer_class = JSONWebTokenSerializer


class VerifyJSONWebToken(JSONWebTokenAPIView):
    """
    验证JWT
    """
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(JSONWebTokenAPIView):
    """
    刷新JWT
    """
    serializer_class = RefreshJSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()

urlpatterns_jwt = [

    url(r'^api/auth/jwt/login/$', obtain_jwt_token, name='login token'),
    url(r'^api/auth/jwt/verify/$', verify_jwt_token, name='verify token'),
    url(r'^api/auth/jwt/refresh/$', refresh_jwt_token, name='refresh token'),

]
