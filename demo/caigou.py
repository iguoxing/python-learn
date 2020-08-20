import urllib.parse
#请求库
import requests
# 解析库
from bs4 import BeautifulSoup
# 用于解决爬取的数据格式化
import io
import sys

keyword='实训平台'
print(keyword)
keyword=urllib.parse.quote(keyword)
print(keyword)

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

# 获取已爬取内容中的td标签内容
data=bs.find_all('a')
print(data)
# 循环打印输出
for i in data:
    print(i.text)
