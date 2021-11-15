#!/usr/bin/env python
# coding: utf-8
'''
ChimesZ Copyright
'''
import requests
import json
import os
import traceback
import time
import sys
import argparse

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'token': os.environ['THU_HOLE_TOKEN']  #更改为自己的token
}
url1 = 'https://tapi.thuhole.com/v3/contents/search?pagesize=50&page={0:d}&keywords={1:s}&device=0&v=v3.0.6-452728' #分别为爬取页数与搜索关键词，无法爬取回复

#url = url1.format(1,'%23nsfw') #在此处修改，默认为nsfw,性相关代码为'%23%E6%80%A7%E7%9B%B8%E5%85%B3'

url_search = 'https://tapi.thuhole.com/v3/contents/post/detail?pid={0:d}&device=0&v=v3.0.6-454542'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='THU Hole spider')
    parser.add_argument('start_id', metavar='start_id', type=int,
            help='the id of hole to start spiding')
    parser.add_argument('end_id', metavar='end_id', type=int,
            help='the id of hole to end spiding')
    parser.add_argument('--path', type=str, default='../data',
            help='the path to store')

    args = parser.parse_args()
    start_id, end_id, data_path = args.start_id, args.end_id, args.path

    for i in range(start_id, end_id+1):
        file_path = f"{data_path}/{i}.json"
        if not os.path.isfile(file_path):
            try:
                url = url_search.format(i)
                r_json = requests.get(url, headers=header).json()

                if r_json['code'] == -101:
                    print("discard ", r_json)
                    continue

                print(r_json)
                with open(file_path, "w", encoding='utf-8') as f:
                    json.dump(r_json, f, ensure_ascii=False, indent='\t')
                time.sleep(2)
            except Exception as e:
                traceback.print_exc()
                i = i-1
                time.sleep(30)

    print("finish!")

