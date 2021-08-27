#!/usr/bin/env python
# coding: utf-8
'''
ChimesZ Copyright
'''
import requests
import json
import os

header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'token':'roaayxqywelaxtezkylpd6li3u22osba'
}
url1 = 'https://tapi.thuhole.com/v3/contents/search?pagesize=50&page={0:d}&keywords={1:s}&device=0&v=v3.0.6-452728' #分别为爬取页数与搜索关键词，无法爬取回复

url = url1.format(1,'%23nsfw') #在此处修改，默认为nsfw,性相关代码为'%23%E6%80%A7%E7%9B%B8%E5%85%B3'


url2 = 'https://i.thuhole.com/'
root = '/Users/apple/Documents/Coding/python_practice/THUHole/nsfw/'

r_json = requests.get(url,headers = header).json()
        
open('nsfw.json','w',encoding='utf-8').write(json.dumps(r_json,ensure_ascii=False,indent=1))
try:
    raw = r_json['data']
except:
    print('树洞负载可能过高，稍后再试')

num = 0

for i in range(0,len(raw)):
    if raw[i]['url'] != "":
        path = root + str(raw[i]['pid'])+'.jpeg'
        img_url = url2 + raw[i]['url']
        print(path)
        if  not os.path.exists(path):
            print(img_url)
            img = requests.get(img_url,timeout=5)
            with open(path,'wb') as f:
                f.write(img.content)
                f.close()
            num = num+1
            print('No.{0:d} success!'.format(num))
        else:
            print('Pic has exsited!')
    else:
        continue