#1.定位到2021必看片
#2.从2021必看片中提取到子页地址
#3.请求子页的地址，拿到下载地址

import requests
import re

ua={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
domain = r'https://dytt89.com/'
resp = requests.get(url=domain,headers=ua,verify=False)#verify=False把安全验证去了

resp.encoding = 'gb2312' #requests模块会默认把爬到的源码用‘utf-8’字符集解码，但电影天堂用的是‘gb2312’，这里指定了字符集

resp.close()
#print(resp.text)

#拿到ul里的li
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
result1 = obj1.finditer(resp.text)
child_href_list=[]
for i in result1:
    ul=i.group('ul')
    # print(ul)

    #提取子页面链接：

    result2 = obj2.finditer(ul)
    for j in result2:
        #拼接子页面url： 主页面域名+子页面href （有些网站要拼接，有的不用）
        child_href = domain + j.group('href').strip('/')
        child_href_list.append(child_href) #把子页面url装到列表里面


#提取子页面内容
obj3 = re.compile(r'◎片　　名(?P<moive>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
for i in child_href_list:
    child_resp = requests.get(i,headers=ua,verify=False)

    child_resp.encoding='gb2312'
    child_resp.close()
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group('moive'),result3.group('download'))
