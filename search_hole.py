#!/usr/bin/env python
# coding: utf-8
'''
ChimesZ Copyright
'''
import requests
import json
import os
from chain_hole import Hole

header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'token':'roaayxqywelaxtezkylpd6li3u22osba'
}
url1 = 'https://tapi.thuhole.com/v3/contents/search?pagesize=50&page={0:d}&keywords={1:s}&device=0&v=v3.0.6-452728' #分别为爬取页数与搜索关键词，无法爬取回复

url = url1.format(1,'%23nsfw') #在此处修改，默认为nsfw,性相关代码为'%23%E6%80%A7%E7%9B%B8%E5%85%B3'

url2 = 'https://i.thuhole.com/'

url3 = 'https://tapi.thuhole.com/v3/contents/post/detail?pid={0:d}&device=0&v=v3.0.6-452742'

root = '/Users/apple/Documents/Coding/python_practice/THUHole/nsfw/' #文件储存位置
if __name__ == '__main__':
    r_json = requests.get(url,headers = header).json()
            
    try:
        raw = r_json['data']
    except:
        print('树洞负载可能过高，稍后再试')
    for i in range(len(raw)):
        print(type(raw[i]['pid']))
        hol = Hole(raw[i]['pid'],url3,header,root,url2)
        hol.get_img()