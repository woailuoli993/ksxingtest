#!/bin/python3
import sys
import re
import json
from urllib import request, parse


def getnumfromstr(strings, ff, fff):
    r = r'{}(\d+){}'.format(ff, fff)
    mylist = re.findall(r, strings)
    return mylist

print('send data....')
# print('find '+sys.argv[1]+'...')
showapi_appid="xxxxxxxxxxxx"
showapi_sign="xxxxxxxxxxxxxxxxxxxxxxxx"
url="http://route.showapi.com/213-1"
send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
                    ,('keyword', '我要你')
                    ,('page', "1")
  ])

req = request.Request(url)
with request.urlopen(req, data=send_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    str_res= f.read().decode('utf-8')
    # print('str_res:',str_res)
    json_res = json.loads(str_res)
    res_body = json_res.get('showapi_res_body')
    songsinfo = res_body['pagebean']['contentlist']
    downlist = list(map(lambda x: x.get('m4a'), songsinfo))
    print(downlist)



