
import requests

api = 'https://music.163.com/api/comment/resource/comments/get'
data = {
    'rid': 'R_SO_4_1841819403',
    'threadId': 'R_SO_4_1841819403',
    'pageNo': 1,
    'pageSize': 20,
    'cursor': -1,
    'offset': 0,
    'orderType': 1
}

resp = requests.get(api,params=data)
json = resp.json()
print(resp.json())