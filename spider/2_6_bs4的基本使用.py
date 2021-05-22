import requests
from bs4 import BeautifulSoup
import csv
ua={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

url = r'http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml'

resp=requests.get(url=url,headers=ua)
# print(resp.text)
resp.close()

#解析数据
#1. 把页面源代码交给BeaurifulSonp解析，生成bs对象

page = BeautifulSoup(resp.text,'html.parser')  #指定html解释器

#2.从bs对象中拿数据
#find(标签，属性=值)
#find_all(标签，属性=值)
# table=page.find('table',class_="hq_table") #由于class是关键字，应该加下划线来区分
table=page.find('table',attrs={'class':"hq_table"}) #此操作可以避免上述情况
print(table)

f = open('菜价.csv' ,mode='w+',encoding='utf-8',newline='')
csvwriter = csv.writer(f)
#拿到所有数据
trs= table.find_all('tr')[1:]
for tr in trs:
    tds = tr.find_all('td') #拿到每行的td
    name= tds[0].text #.text表示被标签的数据
    low = tds[1].text #.text表示被标签的数据
    avg = tds[2].text #.text表示被标签的数据 
    high = tds[3].text #.text表示被标签的数据
    gui = tds[4].text #.text表示被标签的数据
    kind = tds[5].text #.text表示被标签的数据
    date = tds[6].text #.text表示被标签的数据
    # print(name,low,avg,high,gui,kind,date)
    csvwriter.writerow([name,low,avg,high,gui,kind,date])
f.close()
print('over!!!!!!')