import requests
import json
import datetime
import os

user=os.environ['SAKURA_USER']
passwd=os.environ['SAKURA_PASSWD']
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
payload={'email':user,'passwd':passwd}
r = requests.post("https://sakura.kozow.com/auth/login",data=payload)
if r.json()['ret'] == 1:
    checkin = requests.post("https://sakura.kozow.com/user/checkin", cookies=r.cookies)
    if checkin.json()['ret'] == '1':
        print("[",datetime.datetime.now(),"]",checkin.json()['msg'])
    else:
        print("[",datetime.datetime.now(),"]签到失败：",checkin.json()['msg'])
else:
    print("[",datetime.datetime.now(),"]ret=",r.json()['ret']," msg= ",r.json()['msg'])