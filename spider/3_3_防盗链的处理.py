#1.拿到contID
#2.拿到videoStatus返回的json  -> srcURl
#3.srcURL里面的内容进行修整
#4.下载视频
import requests

url = r'https://www.pearvideo.com/video_1640308'
conID =  url.split('_')[-1]
# print(conID)

header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
#防盗链
'Referer':url
}

vedioStatus = r'https://www.pearvideo.com/videoStatus.jsp?contId=%s&mrd=0.7102258115648907'%conID
# print(vedioStatus)
resp = requests.get(vedioStatus,headers=header)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

#真实的视频链接：https://video.pearvideo.com/mp4/adshort/20200108/cont-1640308-14778064_adpkg-ad_hd.mp4
#爬到的视频链接：https://video.pearvideo.com/mp4/adshort/20200108/1621136266960-14778064_adpkg-ad_hd.mp4

srcUrl = srcUrl.replace(systemTime,'cont-'+conID) #处理视频链接
# print(srcUrl)

#下载视频
with open('a.mp4',mode='wb+') as f:
    f.write(requests.get(srcUrl).content) #content转二进制数据
resp.close()