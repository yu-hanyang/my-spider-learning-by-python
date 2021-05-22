#1.找到未加密的参数
#2.想办法把参数进行加密（必须参考网易的逻辑），params,encSecKey
#3.请求网易，拿到评论信息
from Crypto.Cipher import AES

from base64 import b64encode
import json
import requests
url = r'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

#请求方式是POST

data={

'csrf_token': "",
'cursor': "-1",
'offset': "0",
'orderType': "1",
'pageNo': "1",
'pageSize': "20",
'rid': "R_SO_4_1845460977",
'threadId': "R_SO_4_1845460977"
}
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
e="010001"
i= "9IPaKnzlF0Lo0Zjt"

def get_encSecKey():
    return "0d4fd9b2a53e0d68b1876cb54a799b4855553c8baa88f0d8f0c728a692a2d0ef6d25266345ccf8b1c0ba2040821b9dc574632a73fad61800ba3c9ec437c296296053fa2953591b6f7e947855dac859da2081fa7ac37e64d20f3dc41460cde24a1cab321af0a0fdfa7177400ca91fa500fd392f3f8639eceb65e871adf20997dc"

def to_16(data):
    pad = 16-len(data)%16
    data+=chr(pad)*pad
    return data

def get_params(data): #默认接收的是字符串
    fitst = enc_params(data,g)
    second  = enc_params(fitst,i)
    return second #返回params

def enc_params(data,key):#加密过程
    iv="0102030405060708"
    data=to_16(data)

    aes=AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)   #创建加密器
    bs = aes.encrypt(data.encode('utf-8'))#加密，加密的内容的长度必须为16的倍数
    return str(b64encode(bs),'utf-8') #转化成字符串返回

#处理加密过程

header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',

'Referer':'https://music.163.com/song?id=1325905146'
}

resp = requests.post(url=url,data={
    'params':"jarUD7jjFkpw71xrgoQGaO2AUHvzHhknfwznpu3KO0splnaKwpt2GAcUfkFTJIJaYVvmVeJmC9Mc4faMR+feh2wlD+27AigdAN/PLWlzKnGT/XwWh5fRhHozVlNI1Ps4XPo2fA37qDgghfdg3PM8mRp/BN+QBxajxmuxMe/C0dECbiBg/E7/7x6s8MANW/P6cF9pvwnpY6dU+P09ou9sVbQQxU2tlPessPG6GPYR+0XmH+R34vZN4h9WmPNIfIINqZ95KEhklsrDaCwjSsbGrcayR8jahFDHf/JLsYGR/rU=",
    'enSecKey':get_encSecKey()
})


print(resp.text)
