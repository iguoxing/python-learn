# -*- coding: UTF-8 -*-
import xlsxwriter
import datetime
import time

#startTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
#print startTime
startTime1 = time.time()
#print startTime1

workbook = xlsxwriter.Workbook('d:\kami1.xlsx')  #创建一个Excel文件
worksheet = workbook.add_worksheet()               #创建一个sheet

title = [U'名称',U'副标题']     #表格title
worksheet.write_row('A1',title)                    #title 写入Excel

for i in range(1,100):
    num0 = str(i+1)
    num = str(i)
    row = 'A' + num0
    data = [u'学生'+num,num,]
    worksheet.write_row(row, data)
    i+=1

workbook.close()

#time.sleep(60)
#endTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#结束
#print endTime

endTime1 = time.time()
#print endTime1

print(endTime1-startTime1)