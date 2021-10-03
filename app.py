'''
    @date: 2021-10-3
    @author: Li Jinxing

'''
# -*- coding: utf-8 -*-
import requests
import json
import urllib.parse

URL_SESSION = 'http://bjut.sanyth.com:81/nonlogin/qywx/authentication.htm?appId=402880c97b1aa5f7017b1ad2bd97001b&urlb64=L3dlaXhpbi9zYW55dGgvaG9tZS5odG1s'
URL_CLOCKIN = 'http://bjut.sanyth.com:81/syt/zzapply/operation.htm'

# Part0 Read user info
with open('./x.json', 'r') as f:
    core = json.load(f)

# Part1 Get session
s = requests.Session()
response = s.get(URL_SESSION)
session = response.history[0].headers['Set-Cookie'].split(';')[0]

# Part2 Get header & data
HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'bjut.sanyth.com:81',
    'Cookie': session + '; id=' + core['id'] + '; token=' + core['token'],
    "Origin": "http://bjut.sanyth.com:81",

    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)  Mobile/15E148 wxwork/3.1.18 MicroMessenger/7.0.1 Language/zh ColorScheme/Dark'
    'Chrome/85.0.4183.83 Safari/537.36'
}

# user info
info = {
    "xmqkb": {
        "id": "402880c97b1c114b017b1c2af13d02d8"
    },
    "c1": core['c1'],
    "c2": core['c2'],
    "c3": core['c3'],
    "c4": core['c4'],
    "c5": core['c5'],
    "c6": core['c6'],
    "c7": core['c7'],
    "c8": core['c8'],
    "c12": core['c12'],
    "c9": core['c9'],
    "c10": core['c10'],
    "c11": core['c11'],
    "c14": core['c14'],
    "type": "YQSJSB",
    "location_longitude": core['location_longitude'],
    "location_latitude": core['location_latitude'],
    "location_address": core['location_address']
}

# suffix info (static)
suffix_raw = '&msgUrl=syt%2Fzzapply%2Flist.htm%3Ftype%3DYQSJSB%26xmid%3D402880c97b1c114b017b1c2af13d02d8&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB'
# prefix info (user info mostly)
prefix_data = json.dumps(info, ensure_ascii=False)
prefix_raw = 'data='+urllib.parse.quote_plus(prefix_data)
DATA = prefix_raw + suffix_raw
print(DATA)

# Part3 Clock in
response_clockin = requests.post(url=URL_CLOCKIN, headers=HEADER, data=DATA)

if response_clockin.text == 'success':
    print('成功打卡')
else:
    if response_clockin.text == 'Applied today':
        print('今天已经打过卡')
    else:
        print('打卡失败')
