#登录 -> 得到cookie
#带着cookie 去请求url -> 书架上的内容

#以上两个操作必须连续起来
#我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中cookie不会丢失


import requests

#会话
session = requests.session()
data={
    'uesrname': 'admin',
    'password': '123456'
}

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
#1.登录
# url = 'https://passport.17k.com/ck/user/login'
ip = 'http://39.96.217.68:8801/api/private/v1/login'
resp = requests.post(url=ip,data=data,headers=headers)

# print(resp.text)
# print(resp.cookies) 看cookie

#2.拿书架上的数据
#刚才的那个session中是有cookie的

# resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')

print(resp.json())
resp.close()