from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

# class dingUser(AbstractUser):
#     class Meta:
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name
#     DingUserid=models.CharField(max_length=200,verbose_name='钉钉userid')
#
# class DepGroup(Group):
#     class Meta:
#         verbose_name = '用户组'
#         verbose_name_plural = verbose_name
#     DingID = models.CharField(max_length=128,verbose_name='钉钉部门id')
