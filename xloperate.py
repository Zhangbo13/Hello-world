import xlwt
import xlrd
import os
from xlutils.copy import copy

def readExcel(filename,sheetIndex,num=100):
    wb = xlrd.open_workbook(filename)   #读取excel文件，并存入wb变量之中
    sheet = wb.sheet_by_index(sheetIndex)   #按照表的索引读取表，存入sheet变量中，参数若为0，则是第一张表
    list_01= sheet.col_values(0)   #读取第一张表的第一列所有内容，并存入到一个列表list_01中
    list_02= sheet.col_values(1)   #读取第一张表的第二列所有内容，并存入到一个列表list_01中
    list_03= sheet.col_values(2)
    list_04= sheet.col_values(3)
    list_05= sheet.col_values(4)
    tplt = '{:30}\t{:28}\t{:28}\t{:8}\t{:8}'   #设置一个输出表头，包含五个列的表头信息
    print(tplt.format('第一列','第二列','第三列','第四列','第五列'))  #打印表头信心
    count = 0
    for i in range(num):
        print(tplt.format(list_01[count],list_02[count],list_03[count],list_04[count],list_05[count]))
        count += 1




def addToExcel(filename,listall):   #添加列表内容至excel文件中
    if os.path.exists(filename):    #如果文件存在，则执行下面的代码，如果不存在，则执行else中的代码
        rb = xlrd.open_workbook(filename)   #因为文件存在，所以首席按打开文件，生成rb对象
        wb = copy(rb)   #复制rb对象为wb对象
        worksheet = wb.get_sheet(0) #此时wb对象内的sheet可通过get_sheet()来获取，生成一个worksheet对象，此对象可用于添加数据
        nrows = xlrd.open_workbook(filename).sheets()[0].nrows  #由于文件存在，因此是add而不是write，因此首先获取sheet中的行数
        for i in range(len(listall)):   #便历列表，【此例中此列表为嵌套列表，每个子列表中包含4个元素】，可根据需要修改
            try:
                worksheet.write(nrows+i, 0, label=listall[i][0])    #在worksheet中已存在数据的下一行开始添加
                worksheet.write(nrows+i, 1, label=listall[i][1])
                worksheet.write(nrows+i, 2, label=listall[i][2])
                worksheet.write(nrows+i, 3, label=listall[i][3])
            except:
                continue
        os.remove(filename) #删除原文件，后文保存新文件，相当于是复制了一份，因此可以删除，即产生“append”效果
        wb.save(filename)
    else:   #如果文件不存在，则新建一个文件
        filename = filename #新建文件的名称
        workbook = xlwt.Workbook(encoding='utf-8')  #新建workbook
        worksheet = workbook.add_sheet('my_worksheet')  #在workbook中新建worksheet
        nrows = 1   #留出第一行用于存放标题
        for i in range(len(listall)):
            try:    #添加数据
                worksheet.write(nrows+i, 0, label=listall[i][0])
                worksheet.write(nrows+i, 1, label=listall[i][1])
                worksheet.write(nrows+i, 2, label=listall[i][2])
                worksheet.write(nrows+i, 3, label=listall[i][3])
            except:
                continue
        workbook.save(filename)

