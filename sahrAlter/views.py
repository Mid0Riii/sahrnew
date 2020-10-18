from django.shortcuts import render, get_object_or_404,HttpResponse,redirect
from django.http.response import JsonResponse
import requests
import random
from django.contrib.auth.models import User
from django.contrib.auth import login

def login_dingding(request):
    if request.method == "GET":
        code = request.GET.get('code', )
        state = request.GET.get('state', )
        # 开发环境
        appId = 'dingoa2lwgjotltr4zrlmh'
        appSecret = 'QHwsP0NvOS4ibNFQjlS7FHb2BselT-aLkJV-SPgRpQVGvDTK-LL3UhP7pv3jvr9y'
        # 生产环境
        #appId = 'dingoaonyvme31pxjsv9kt'
        #appSecret = '8TgBpb1Ktud6y_jOvflXG5zXdkfpjvYxrKz9LH_zD4HIWUFbVGOOtMzjM0qWrUk8'

        token = requests.get(f'https://oapi.dingtalk.com/sns/gettoken?appid={appId}&appsecret={appSecret}')
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
            user = User.objects.get(username=user_info['unionid'])
        except Exception as e:
            password = f'{random.randint(1000,99999)}'
            try:
                user = User.objects.create(username=user_info['unionid'], password=password,
                                           first_name=user_info['nick'],is_staff=True,is_superuser=True)
            except Exception as e:
                user = User.objects.create(username=f"{user_info['unionid']}{random.randint(0,9999)}", password=password,
                                           first_name=user_info['nick'],is_staff=True,is_superuser=True)

        finally:
            login(request, user)
            request.session['is_staff'] = True
            login_ip = request.META['REMOTE_ADDR']

        return redirect('/ncusc/hr/currentstaff')