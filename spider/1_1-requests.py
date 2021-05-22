import requests

url = r'https://www.sogou.com/web?query=周杰伦'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
resp =requests.get(url,headers=headers)

resp.close()#防止被封


print(resp.text) #text拿源码