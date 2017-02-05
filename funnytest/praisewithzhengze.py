#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 05/02/2017
import re


# ff(\d+)fff
def getnumfromstr(strings, ff, fff):

    r = r'{}(\d+){}'.format(ff, fff)
    mylist = re.findall(r, strings)
    return mylist


if __name__ == '__main__':
    a = "abcff23423fffsfertgrff234234fffwvgwegweff444fffwerwegrewff13244fff"
    b = getnumfromstr(a, 'ff', 'fff')

    with request.urlopen(req, data=send_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        str_res = f.read().decode('utf-8')
        print('str_res:', str_res)
        json_res = json.dumps(str_res)
        #  获取所有歌曲的下载地址
        showapi_res_body = json_res.get()

        print ('json_res data is:', json_res)
