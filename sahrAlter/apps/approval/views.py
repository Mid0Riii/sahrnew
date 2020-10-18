from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from .models import Signs
from django.contrib.auth.models import Group
# from DingLogin.models import DepGroup
# Create your views here.

def create_sign(request):
    if request.method=='POST':
        Signs.objects.create(title=request.POST['title'],createDate=request.POST['createDate'],createAca='软件学院',
                            director=request.POST['director'],info=request.POST['info'],dep_person=request.POST['dep_person'],
                            status_code='100')
        return HttpResponse("签单添加成功")
    return render(request,'create_sign_view.html')

def detail_sign(request,pk):
    sign = get_object_or_404(Signs,pk=pk)
    dic={
        "title":sign.title,
        "createDate":sign.createDate,
        "createAca":sign.createAca,
        "director":sign.director,
        "info":sign.info,
        "dep_person":sign.dep_person,
        "dep_opinion":sign.dep_opinion,
        "dep_judge":sign.dep_judge,
        "office_opinion":sign.office_opinion,
        "office_judge":sign.office_judge,
        "relate_opinion":sign.relate_opinion,
        "relate_judge":sign.relate_judge,
        "vice_opinion":sign.vice_opinion,
        "vice_judge":sign.vice_judge,
        "aca_opinion":sign.aca_opinion,
        "aca_judge":sign.aca_judge,
        "status_code":sign.status_code,
    }
    for key in dic:
        if str(dic[key]) == 'None':
            dic[key] = ''
    return render(request,'detail_sign_view.html',{"dic":dic})


def edit_sign(request,pk):
    sign = get_object_or_404(Signs,pk=pk)
    sign_current_status = sign.status_code
    if request.method=='POST':
        if sign_current_status == '100':
            sign.dep_opinion=request.POST['dep_opinion']
            judge = request.POST['dep_judge']
            if judge == '驳回':
                sign.status_code = '000'
            else:
                sign.status_code = '101'
            sign.dep_judge = judge
            sign.save()
        if sign_current_status == '101':
            sign.office_opinion=request.POST['office_opinion']
            judge = request.POST['office_judge']
            if judge == '驳回':
                sign.status_code = '000'
            else:
                sign.status_code = '102'
            sign.office_judge = judge
            sign.save()
        if sign_current_status == '102':
            sign.relate_opinion=request.POST['relate_opinion']
            judge = request.POST['relate_judge']
            if judge == '驳回':
                sign.status_code = '000'
            else:
                sign.status_code = '103'
            sign.relate_judge = judge
            sign.save()
        if sign_current_status == '103':
            sign.vice_opinion=request.POST['vice_opinion']
            judge = request.POST['vice_judge']
            if judge == '驳回':
                sign.status_code = '000'
            else:
                sign.status_code = '104'
            sign.vice_judge = judge
            sign.save()
        if sign_current_status == '104':
            sign.aca_opinion=request.POST['aca_opinion']
            judge = request.POST['aca_judge']
            if judge=='驳回':
                sign.status_code='000'
            else:
                sign.status_code='200'
            sign.aca_judge=judge
            sign.save()
        return HttpResponse("操作成功")
    username = request.user
    usergroup=Group.objects.get(user=username)
    # 000 签单驳回 100部门审批 101两办审批 102相关部门审批 103分管校领导审批 104校领导审批 200通过
    group_code={
        "部门负责人":"100",
        "两办":"101",
        "相关部门":"102",
        "分管校领导":"103",
        "校领导":"104",
    }
    group_list=['部门负责人','两办','相关部门','分管校领导','校领导']
    try:
        if sign_current_status != group_code[str(usergroup)]:
            return HttpResponse("您无权操作当前签单")
    except:
        return HttpResponse("您无权操作当前签单")
    dic = {
            "id":sign.pk,
            "title": sign.title,
            "createDate": sign.createDate,
            "createAca": sign.createAca,
            "director": sign.director,
            "info": sign.info,
            "dep_person": sign.dep_person,
            "dep_opinion": sign.dep_opinion,
            "dep_judge": sign.dep_judge,
            "office_opinion": sign.office_opinion,
            "office_judge": sign.office_judge,
            "relate_opinion": sign.relate_opinion,
            "relate_judge": sign.relate_judge,
            "vice_opinion": sign.vice_opinion,
            "vice_judge": sign.vice_judge,
            "aca_opinion": sign.aca_opinion,
            "aca_judge": sign.aca_judge,
            "status_code": sign.status_code,
        }
    for key in dic:
        if str(dic[key]) == 'None':
            dic[key] = ''
    if sign.status_code !='200'or sign.status_code!='000':
        return render(request,'update_sign_view.html',{"dic":dic})
    else:
        return render(request,'detail_sign_view.html',{"dic":dic})
