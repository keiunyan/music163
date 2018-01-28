# -*- coding:utf-8 -*-

import os
import io
import re
import sys
import json
import lxml
import requests
from bs4 import BeautifulSoup

def main(url):
    req_header={
	"Host": "music.163.com",\
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",\
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",\
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
	"Accept-Encoding": "gzip, deflate",\
	"Referer": "http://music.163.com/",\
	"Connection": "keep-alive",\
	"Upgrade-Insecure-Requests": "1"}
    s=requests.session()
    r=s.get(url, headers=req_header);
    html=r.text

    """
    #使用正则分析
    #strs=re.findall( r'<dt><i class="u-icn u-icn-[0-9]+"></i>(.+)</dt>', html, re.M)
    #strs=re.findall( r'<a class="s-fc1 " href="/discover/playlist/\?cat=.*" data-cat=".+">.+</a>', html, re.M)
    # 风格
    p=re.compile('<a class="s-fc1 " href="/discover/playlist/\?cat=.*" data-cat=".+">(.+)</a>'); 
    # 歌单
    p=re.compile('<a title=".*" href="/playlist\?id=\d+" class="tit f-thide s-fc0">(.*)</a>')
    strs=p.findall(html, re.M)
    for str in strs:
        print(str)
    """

    # 使用BeautifulSoup分析
    #soup = BeautifulSoup(html,"html.parser")
    soup = BeautifulSoup(html,"lxml")
    for a in soup.find_all('a', href=re.compile("^/playlist\?id=\d+"), attrs={"class":"tit f-thide s-fc0"}):
        print(a.get('href'),a.get('title'))

    
if __name__ == "__main__":
    main("http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=0");

