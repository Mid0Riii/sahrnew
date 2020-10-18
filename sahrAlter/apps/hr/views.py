from .models import Staff, Department,Meal_allow

from .serializers import StaffSerializer, DepSerializer
from rest_framework import generics
from django.core import serializers
import datetime
from django.shortcuts import render, get_object_or_404,HttpResponse,redirect
from django.http.response import JsonResponse
import requests
import random
from django.contrib.auth.models import User
from django.contrib.auth import login

def dep_form_iframe(request,pk):
    obj = get_object_or_404(Department,pk=pk)
    dep = {
        'name':obj.name,
        'director':obj.director,
        'createTime':obj.createTime,
        'info':obj.info
    }
    staffs = Staff.objects.filter(work_department_id=pk)
    return render(request, 'dep_iframe.html',locals())


def staff_form_iframe(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    dic = {
        'id':pk,
        'name': obj.personal_name,
        'gender': obj.personal_gender,
        'idn_num': obj.personal_id_num,
        'birth_date': obj.personal_birth_date,
        'enter_date': obj.work_enter_date,
        'hire_method': obj.work_hire_method,
        'on_market': obj.personal_on_market,
        'soc_ins': obj.personal_soc_ins,
        'soc_ins_num': obj.personal_soc_ins_id,
        'department': obj.work_department,
        'duty': obj.work_duty,
        'duty_hire_date': obj.work_duty_hire_date,
        'set_rank_date': obj.work_set_rank_date,
        'hire_rank_aca_date': obj.work_hire_rank_aca_date,
        'position': obj.work_position,
        'title': obj.work_title,
        'edu_background': obj.edu_background,
        'edu_grade': obj.edu_grade,
        'is_marry': obj.personal_is_marry,
        'status': obj.personal_status,
        'folk': obj.personal_folk,
        'reg_location': obj.personal_reg_location,
        'phone': obj.personal_phone,
        'phone_other': obj.personal_phone_other,
        'emer_people': obj.personal_emer_people,
        'emer_phone': obj.personal_emer_phone,
        'more': obj.other_more,
        'learn_exp': obj.edu_learn_exp,
        'current_location': obj.personal_current_location,
        'edu_collage_school':obj.edu_collage_school,
        'edu_undergraduate_school': obj.edu_undergraduate_school,
        'edu_master_school': obj.edu_master_school,
        'edu_doctor_school': obj.edu_doctor_school,
        'edu_postdoctor_school':obj.edu_postdoctor_school,
        'avatar': '/media/' + str(obj.other_avatar),
    }
    for key in dic:
        if str(dic[key]) == 'None':
            dic[key] = ''
    # dic = {'format':format}
    # return render(request,'list_form_iframe.html',dic)
    return render(request, 'list_form_iframe.html', {'dic': dic})


def Meal_personal(request,pk):
    obj = Meal_allow.objects.filter(date__year=pk)
    names=[]
    datas=[]
    yearTotal=0
    monthTotalList=[]
    json = {"statistics":list}
    for person in obj:
        if person.name not in names:
            names.append(person.name)
    for name in names:
        mouthCountList = []
        total=0
        for i in range(1,13):
            mouthCountSet = Meal_allow.objects.filter(name=name,date__month=i)
            mouth=0
            for mouthCount in mouthCountSet:
                mouth += int(mouthCount.consume)
                total+=int(mouthCount.consume)
            mouthCountList.append(mouth)
        personalDic={
            "name":name,
            "money":mouthCountList,
            "total":total,
        }
        datas.append(personalDic)
    for i in range(1,13):
        monthTotal=0
        monthTotalSet = Meal_allow.objects.filter(date__month=i)
        for month in monthTotalSet:
            yearTotal+=int(month.consume)
            monthTotal+=int(month.consume)
        monthTotalList.append(monthTotal)
    monthTotalList.append(yearTotal)
    return JsonResponse({"staff":datas,"total":monthTotalList})


# 用来生成年度选项
def Meal_statistic(request):
    latestYear=''
    earliestYear=''
    latest = Meal_allow.objects.order_by('-date')[:1]
    earliest = Meal_allow.objects.order_by('date')[:1]
    for i in latest:
        latestYear=i.date.year
    for j in earliest:
        earliestYear = j.date.year
    rangeYear = list(range(earliestYear,latestYear+1))
    dic={
        'rangeYear':rangeYear
    }
    return render(request,'meal_statistic_iframe.html',dic)

# DRF内容，目前无用
# ------------------------------------------------------------------------------------
# 易于理解的写法
# class staff_list(APIView):
#
#    def get(self, request, format=None):
#        staffs = Staff.objects.all()
#        serializer = StaffSerializer(staffs, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, fromat=None):
#        serializer = StaffSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 用mixed-in重构
class staff_list(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class staff_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class dep_list(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer


class dep_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer
# ----------------------------------------------------------------------------------------
