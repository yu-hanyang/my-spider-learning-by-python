import re
import requests
import csv
ua={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
param={
    'start':'',
    'filter':''
}
url = r'https://movie.douban.com/top250'

resp = requests.get(url,headers=ua,params=param)

resp.close()
page_content=resp.text


#解析数据
obj_film_name = re.compile(r'<li>.*?<span class="title">(?P<film_name>.*?)'
                           r'</span>.*?<p class="">.*?<br>(?P<years>.*?)&nbsp.*?<span class="rating_num" '
                            r'property="v:average">(?P<rating_num>.*?)</span>'
                           r'.*?<span>(?P<people>.*?)</span>',re.S)

result = obj_film_name.finditer(page_content)
f = open('data.csv', mode='w+',encoding='utf-8')
csvwriter = csv.writer(f)
for i in result:
    # print(i.group('film_name')+'----'+i.group('years').strip()+'----'+i.group('rating_num')+'----'+i.group('people'))
    d = i.groupdict()
    d['years']=d['years'].strip()
    csvwriter.writerow(d.values())
f.close()
print('over!')


