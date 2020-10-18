from xadmin.views import CommAdminView
from django.shortcuts import render
from django.http import HttpResponse
import xlrd
import xlwt
import time
import io


def CountDutyPerson(file, type):
    if type == "xls":
        data = xlrd.open_workbook(filename=None, file_contents=file.read(), formatting_info=True)
    elif type == "xlsx":
        data = xlrd.open_workbook(filename=None, file_contents=file.read())
    table = data.sheet_by_index(0)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('工作表1')
    worksheetrow = 1
    worksheet.write(0, 0, '姓名')
    worksheet.write(0, 1, '打卡时间')
    for rowindex in range(0, table.nrows):
        row = table.row_values(rowindex)
        name = row[1]
        rawtime = row[3].split(" ")[-1]
        realtime = time.strptime(rawtime, "%H:%M:%S")
        starttime1 = time.strptime("18:30:00", "%H:%M:%S")
        endtime1 = time.strptime("19:30:00", "%H:%M:%S")
        starttime2 = time.strptime("22:15:00", "%H:%M:%S")
        endtime2 = time.strptime("23:00:00", "%H:%M:%S")
        if realtime > starttime1 and realtime < endtime1:
            worksheet.write(worksheetrow, 0, name)
            worksheet.write(worksheetrow, 1, row[3])
            worksheetrow += 1
        if realtime > starttime2 and realtime < endtime2:
            worksheet.write(worksheetrow, 0, name)
            worksheet.write(worksheetrow, 1, row[3])
            worksheetrow += 1
    output = io.BytesIO()  # 创建在内存中处理对象
    workbook.save(output)
    return output


class CountDutyView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "小工具"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/ncusc/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        return render(request, 'count-duty.html', context)  # 最后指定自定义的template模板，并返回context

    def post(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "小工具"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/ncusc/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        myFile = request.FILES.get("myfile", None)
        if (myFile.name).split(".")[-1] == "xls":
            output = CountDutyPerson(myFile, "xls")
        elif (myFile.name).split(".")[-1] == "xlsx":
            output = CountDutyPerson(myFile, "xls")

        res = HttpResponse()
        res["Content-Type"] = "application/octet-stream"
        res["Content-Disposition"] = 'filename="result.xlsx"'
        res.write(output.getvalue())

        return res
