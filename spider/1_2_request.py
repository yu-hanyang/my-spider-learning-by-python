import requests

url = 'https://fanyi.baidu.com/sug'

ua={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

s=input('请输入你要翻译的英文单词：')

dat={
    'kw':s
}

#发送post清求，发送的数据必需放在字典中，通过data进行传递
resp = requests.post(url,data=dat,headers=ua)
resp.close()
print(resp.json()) #将服务器返回的数据转换成json() =>python 字典