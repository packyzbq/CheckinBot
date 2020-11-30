import requests
import json
import datetime
import os
from bs4 import BeautifulSoup

url_getter="https://poi.aoao.me/"
r = requests.get(url_getter)
soup = BeautifulSoup(r.text,'html.parser')
url = soup.a.text

user=os.environ['SAKURA_USER']
passwd=os.environ['SAKURA_PASSWD']
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
payload={'email':user,'passwd':passwd}
r = requests.post("https://"+ url +"/auth/login",data=payload)
if r.json()['ret'] == 1:
    checkin = requests.post("https://"+ url +"/user/checkin", cookies=r.cookies)
    if checkin.json()['ret'] == '1':
        print("[",datetime.datetime.now(),"]",checkin.json()['msg'])
    else:
        print("[",datetime.datetime.now(),"]签到失败：",checkin.json()['msg'])
else:
    print("[",datetime.datetime.now(),"]ret=",r.json()['ret']," msg= ",r.json()['msg'])