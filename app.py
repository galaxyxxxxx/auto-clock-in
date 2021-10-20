# -*- coding: utf-8 -*-
'''
@date: 2021-10-3
@author: Li Jinxing, Chu Yumo
'''
import requests
import json
import urllib.parse
from os import environ
from email.mime.text import MIMEText
import smtplib

# Email notify
EMAIL = environ['EMAIL']
if EMAIL:
    EMAIL_USERNAME = environ['EMAIL_USERNAME']
    EMAIL_TO = environ['EMAIL_TO']
    EMAIL_FROM = environ['EMAIL_FROM']
    EMAIL_PASSWORD = environ['EMAIL_PASSWORD']
    EMAIL_SERVER = environ['EMAIL_SERVER']
    EMAIL_PORT = int(environ['EMAIL_PORT'])

URL_CLOCKIN = 'http://bjut.sanyth.com:81/syt/zzapply/operation.htm'

# Part0 Read user info
with open('./info.json', 'r') as f:
    core = json.load(f)

s = requests.Session()
s.cookies.set("id", core['id'])
s.cookies.set("token", core['token'])
s.cookies.set("JSESSIONID", core['JSESSIONID'])
HEADER = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'bjut.sanyth.com:81',
    'Origin': 'http://bjut.sanyth.com:81',
    'Referer': 'http://bjut.sanyth.com:81/webApp/xuegong/index.html',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)  Mobile/15E148 wxwork/3.1.18 MicroMessenger/7.0.1 Language/zh ColorScheme/Dark'
                  'Chrome/85.0.4183.83 Safari/537.36',
    'X-Requested-With': 'com.tencent.wework',
}

# info = core
# info['xmqkb'] = {
#         'id': '402880c97b1c114b017b1c2af13d02d8'
#     }
info = {
    'xmqkb': {
        'id': '402880c97b1c114b017b1c2af13d02d8'
    },
    'c1': core['c1'],
    'c2': core['c2'],
    'c3': core['c3'],
    'c4': core['c4'],
    'c5': core['c5'],
    'c6': core['c6'],
    'c7': core['c7'],
    'c8': core['c8'],
    'c12': core['c12'],
    'c9': core['c9'],
    'c10': core['c10'],
    'c11': core['c11'],
    'c14': core['c14'],
    'type': 'YQSJSB',
    'location_longitude': core['location_longitude'],
    'location_latitude': core['location_latitude'],
    'location_address': core['location_address']
}

# suffix info (static)
suffix_raw = '&msgUrl=syt%2Fzzapply%2Flist.htm%3Ftype%3DYQSJSB%26xmid%3D402880c97b1c114b017b1c2af13d02d8&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB'
# prefix info (user info mostly)
prefix_data = json.dumps(info, ensure_ascii=False)
prefix_raw = 'data=' + urllib.parse.quote_plus(prefix_data)
DATA = prefix_raw + suffix_raw

# Part3 Clock in
response_clockin = s.post(url=URL_CLOCKIN, headers=HEADER, data=DATA)

result = '打卡失败'

if response_clockin.text == 'success':
    result = '打卡成功'
else:
    if response_clockin.text == 'Applied today':
        result = '今天已经打过卡'
    else:
        result += f'''
HTTP status: {response_clockin.status_code}
打卡数据:
{
    json.dumps(info, ensure_ascii=False, sort_keys=True, indent=2)
}
{
    DATA
}
{session}
'''

if EMAIL:
    message = MIMEText(result, 'plain', 'utf-8')
    message['Subject'] = '打卡结果'
    message['FROM'] = EMAIL_FROM
    message['To'] = EMAIL_TO

    server = smtplib.SMTP(EMAIL_SERVER)
    server.connect(EMAIL_SERVER, EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USERNAME, [EMAIL_USERNAME], message.as_string())
else:
    print(result)
