import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime


class BaseModelMixin(models.Model):
    deleted = models.BooleanField(verbose_name="是否被删除", default=False)
    created_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.datetime.now)
    updated_time = models.DateTimeField(verbose_name=u"更新时间", default=datetime.datetime.now)

    class Meta:
        abstract = True


class OwnerMixin(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="所有者")

    class Meta:
        abstract = True
