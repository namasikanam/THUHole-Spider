#!/usr/bin/env python
# coding: utf-8
'''
ChimesZ
'''
import requests
import json
import os
import re
import time

header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'token':'your_token'
}

url = 'https://tapi.thuhole.com/v3/contents/post/detail?pid={0:d}&device=0&v=v3.0.6-452742'
url1 = 'https://i.thuhole.com/'

root = '/Users/apple/Documents/Coding/python_practice/THUHole/hole/'

class Hole:
    def __init__(self,pid,url,header,root,url1) -> None:
        self.pid = int(pid)
        self.url = str(url)
        self.header = header
        self.root = str(root)
        self.url1 = str(url1)

    def get_json(hole)->dict:
        url = hole.url.format(hole.pid)
        r_json = requests.get(url,headers=hole.header).json()
        return r_json

    @staticmethod
    def download_img(reply,num,id):
        if reply['url'] != "":
                path = hole.root + str(reply[id])+'.jpeg'
                img_url = hole.url1 + reply['url']
                print(path)
                if not os.path.exists(path):
                    print(img_url)
                    img = requests.get(img_url,timeout=5)
                    with open(path,'wb') as f:
                        f.write(img.content)
                        f.close()
                        num = num + 1
                    print('No.{0:d} success!'.format(num))
                else:
                    print('Pic has exsited!')
        else:
            pass
        return num
    
    def get_img(hole):
        data = hole.get_json()['data']
        post = hole.get_json()['post']
        num = 0
        num = hole.download_img(post,num,'pid')
        for reply in data:
            num = hole.download_img(reply,num,'cid')
        if num == 0:
            print('No Picture Exists!')
    
    def get_pid(hole):
        text = hole.get_json()['post']['text']
        re_str = r'#(\d+)'
        if re.findall(re_str,text) != []:
            pid = int(re.findall(re_str,text)[0])
            return pid
        else:
            return False

if __name__ == '__main__':
    hole = Hole(451146,url,header,root,url1)
    hole.get_img()
    while hole.get_pid():
        pid = hole.get_pid()
        hole = Hole(pid,url,header,root,url1)
        hole.get_img()
        print('--------#{0:d}Finished!------'.format(hole.pid))
        time.sleep(5)
    print('---------**END**----------')#结束于#406088
