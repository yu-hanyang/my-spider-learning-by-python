#原理.通过第三方的机器去请求
import requests

#1.181.48.68:3128 #冒号前面是IP后面是端口
proxies = {
    'https':r'http://1.181.48.68:3128',
    'http':''
}

url = r'https://ui.cn.w.kunlunca.com/?*Cvd9B1Q5pdLi9fdHBsLzEvNS8/dXNlcj0wZGgxWFM='
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
i=0
while True:
    resp = requests.get(url=url,proxies=proxies,headers=header)
    resp1 = requests.get(url=url,proxies=proxies,headers=header)
    resp2= requests.get(url=url,proxies=proxies,headers=header)
    resp3 = requests.get(url=url,proxies=proxies,headers=header)
    resp4 = requests.get(url=url,proxies=proxies,headers=header)
    resp5 = requests.get(url=url,proxies=proxies,headers=header)
    resp6 = requests.get(url=url,proxies=proxies,headers=header)
    resp7 = requests.get(url=url,proxies=proxies,headers=header)
    resp8 = requests.get(url=url,proxies=proxies,headers=header)
    resp9 = requests.get(url=url,proxies=proxies,headers=header)
    resp10 = requests.get(url=url,proxies=proxies,headers=header)
    resp11 = requests.get(url=url,proxies=proxies,headers=header)
    resp12 = requests.get(url=url,proxies=proxies,headers=header)
    resp13 = requests.get(url=url,proxies=proxies,headers=header)
    resp14 = requests.get(url=url,proxies=proxies,headers=header)
    resp45 = requests.get(url=url,proxies=proxies,headers=header)

    i+=1
    print(i)