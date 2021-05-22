import requests

url = 'https://movie.douban.com/j/chart/top_list'#原url https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20

#当url中’？‘后面的参数特别长的时候，可以重新封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': '0',
    'limit': '20',

}

ua={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

resp =requests.get(url=url,params=param,headers=ua)
resp.close()
print(resp.request.url)
print(resp.json())