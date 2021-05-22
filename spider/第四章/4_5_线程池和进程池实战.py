#1.如何提取单个页面的数据
#2.上线程池，多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f=open('data.csv',mode='w',encoding='utf-8',newline='')
csvwriter=csv.writer(f)
def download_one_page(url):
    resp = requests.get(url)
    resp.close()
    html = etree.HTML(resp.text)
    table = html.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]
   # trs = table.xpath('./tr')[1:]
    trs = table.xpath('./tr[position()>1]')[1:]
    for tr in trs:
        txt= tr.xpath('./td/text()')
        txt=(item.replace('\\','').replace('/','') for item in txt)
        csvwriter.writerow(list(txt))
    print(url,'提取完毕')


if __name__ == '__main__':
    # download_one_page('http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml')
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            #把任务给线程池
            t.submit(download_one_page,f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    print('全部下载完毕')

f.close()