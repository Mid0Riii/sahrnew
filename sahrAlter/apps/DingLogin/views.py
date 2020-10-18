from django.shortcuts import render, get_object_or_404,HttpResponse,redirect
from django.http.response import JsonResponse
import requests
import random
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings

from django.contrib.auth import get_user_model

import requests
import random
# from .models import DepGroup, dingUser
# from django.contrib.auth.models import User
from django.contrib.auth import login
from django.conf import settings
from hr.models import Department, Staff

User = get_user_model()
def get_app_accesstoken():
    appId = settings.DINGAPPID
    appsecret = settings.DINGAPPSECRET
    token = requests.get(f'https://oapi.dingtalk.com/gettoken?appkey={appId}&appsecret={appsecret}')
    app_access_token = token.json()["access_token"]
    return app_access_token


def get_dep_list(app_access_token):
    token = requests.get(f'https://oapi.dingtalk.com/department/list?access_token={app_access_token}')
    if __name__ == '__main__':
        print(token.json())
    return token.json()['department']


def get_dep_staff_list(app_access_token, depDingID):
    token = requests.get(
        f"https://oapi.dingtalk.com/user/simplelist?access_token={app_access_token}&department_id={depDingID}")
    return token.json()['userlist']


def get_staff_detail(app_access_token, userid):
    token = requests.get(f"https://oapi.dingtalk.com/user/get?access_token={app_access_token}&userid={userid}")
    return token.json()


def update_user_group(dep):
    depName = dep['name']
    depDingID = dep['id']
    try:
        groupObj = DepGroup.objects.get(DingID=depDingID)
        groupObj.name = depName
    except Exception as e:
        groupObj = DepGroup.objects.create(name=depName, DingID=depDingID)
    return groupObj


def update_department(dep):
    depName = dep['name']
    depDingID = dep['id']
    try:
        depObj = Department.objects.get(DingID=depDingID)
        depObj.DingID = depDingID
        depObj.name = depName
        depObj.save()
    except Exception as e:
        depObj = Department.objects.create(name=depName, DingID=depDingID)
    return depObj


def update_staff(staff, depObj):
    staffID = staff['userid']
    staffName = staff['name']
    try:
        staffObj = Staff.objects.get(DingID=staffID)
        staffObj.personal_name = staffName
        staffObj.save()
    except Exception as e:
        staffObj = Staff.objects.create(personal_name=staffName, DingID=staffID)
        staffObj.work_department.add(depObj)


def update_user(staff,groupObj):
    staffID = staff['userid']
    staffName = staff['name']
    try:
        user = dingUser.objects.get(username=staffName)
    except Exception as e:
        password = f'{random.randint(1000, 99999)}'
        try:
            user = dingUser.objects.create(username=staffName, password=password,DingUserid=staffID,
                                       first_name=staffName, is_staff=True, is_superuser=True)
        except Exception as e:
            user = dingUser.objects.create(username=f"{staffName}{random.randint(0, 9999)}", password=password,DingUserid=staffID,
                                       first_name=staffName, is_staff=True, is_superuser=True)
    user.groups.add(groupObj)


def migrate_from_dingding(request):
    access_token = get_app_accesstoken()
    depList = get_dep_list(access_token)
    # print(depList)
    for dep in depList:
        depObj = update_department(dep)
        groupObj=update_user_group(dep)
        staffList = get_dep_staff_list(access_token, dep['id'])
        for staff in staffList:
            update_staff(staff, depObj)
            update_user(staff,groupObj)
    return HttpResponse("<h1>更新完成</h1>")



def login_dingding(request):
    if request.method == "GET":
        code = request.GET.get('code', )
        state = request.GET.get('state', )
        appId=settings.DINGLOGINAPPID
        appSecret=settings.DINGLOGINAPPSECRET
        token = requests.get(f'https://oapi.dingtalk.com/sns/gettoken?appid={appId}&appsecret={appSecret}')
        print(token.json())
        access_token = token.json()["access_token"]

        tmp_auth_code = requests.post(f"https://oapi.dingtalk.com/sns/get_persistent_code?access_token={access_token}",
                                      json={
                                          "tmp_auth_code": code
                                      })
        tmp_code = tmp_auth_code.json()
        print(tmp_code)
        openid = tmp_code['openid']
        persistent_code = tmp_code['persistent_code']

        sns_token_request = requests.post(f"https://oapi.dingtalk.com/sns/get_sns_token?access_token={access_token}",
                                          json={
                                              "openid": openid,
                                              "persistent_code": persistent_code
                                          })

        sns_token = sns_token_request.json()['sns_token']

        user_info_request = requests.get(f'https://oapi.dingtalk.com/sns/getuserinfo?sns_token={sns_token}')

        user_info = user_info_request.json()['user_info']
        print(user_info)
        try:
            nuser = User.objects.get(username=user_info['unionid'])
        except Exception as e:
            password = f'{random.randint(1000,99999)}'
            try:
                nuser = User.objects.create(username=user_info['nick'], password=password,
                                           first_name=user_info['nick'],is_staff=True,is_superuser=True)
            except Exception as e:
                nuser = User.objects.create(username=f"{user_info['unionid']}{random.randint(0,9999)}", password=password,
                                           first_name=user_info['nick'],is_staff=True,is_superuser=True)

        finally:
            login(request, nuser)
            request.session['is_staff'] = True
            login_ip = request.META['REMOTE_ADDR']

        return redirect('/ncusc/hr/currentstaff')