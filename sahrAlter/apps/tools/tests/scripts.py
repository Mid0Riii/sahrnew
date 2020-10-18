import xlrd
import xlwt
import time

def CountDutyPerson(data,type):
    data = xlrd.open_workbook(filename=None,file_contents=data.read,)
    table = data.sheet_by_index(0)
    for rowindex in range(0,table.nrows):
        row = table.row_values(rowindex)
        name = row[1]
        rawtime = row[3].split(" ")[-1]
        realtime = time.strptime(rawtime,"%H:%M:%S")
        starttime1 = time.strptime("18:30:00","%H:%M:%S")
        endtime1 = time.strptime("19:30:00", "%H:%M:%S")
        starttime2 = time.strptime("22:15:00", "%H:%M:%S")
        endtime2 = time.strptime("23:00:00", "%H:%M:%S")
        if realtime>starttime1 and realtime<endtime1:
            print(rawtime)
            print(name)

        if realtime>starttime2 and realtime<endtime2:
            print(rawtime)
            print(name)

if __name__=='__main__':
    CountDutyPerson("软件学院-2020-08.xls")
