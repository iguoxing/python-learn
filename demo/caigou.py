import urllib.parse
#请求库
import requests
# 解析库
from bs4 import BeautifulSoup
# 用于解决爬取的数据格式化
import io
import sys
# 表格
import xlsxwriter
import datetime
import time

startTime1 = time.time()

keyword='实训平台'
print(keyword)
keyword=urllib.parse.quote(keyword)
# print(keyword)

url='http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1' \
    '&start_time=&end_time=&timeType=2&searchparam=&searchchannel=0&dbselect=bidx&' \
    'kw='+keyword+'&bidSort=0&pinMu=0&bidType=0&buyerName=&projectId=&displayZone=&zoneId=&agentName=';

kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
      'referer': 'https://www.mzitu.com/',
      'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1575636408; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1575636892'}

req = requests.get(url,headers = kv)
result = req.content.decode('utf-8')

# 再次封装，获取具体标签内的内容
bs = BeautifulSoup(result,'html.parser')
# # 具体标签
# print("解析后的数据")
# print(bs.span)

# 获取已爬取内容中的a标签内容
obj=bs.find_all('div',{'class':'vT-srch-result'})
data=obj[0].find_all('a')
# print(data)
projects=[]
# 循环处理数据
for i in data:
    if(i['href']!='javascript:void(0)'):
        projects.append([i.text.strip(), i['href']])

# print(projects)
# print(len(projects))

workbook = xlsxwriter.Workbook('d:\zhaobiao-0822-2.xlsx')  #创建一个Excel文件
worksheet = workbook.add_worksheet()               #创建一个sheet

title = [U'标题',U'链接']     #表格title
worksheet.write_row('A1',title)                    #title 写入Excel

for i in range(len(projects)):
    num0 = str(i+2)
    name = str(projects[i][0])
    link = str(projects[i][1])
    row = 'A' + num0
    data = [name,link,]
    worksheet.write_row(row, data)
    i+=1

workbook.close()

endTime1 = time.time()

print(endTime1-startTime1)

