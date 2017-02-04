#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-11-30
import requests
import xml.etree.ElementTree as ET
import os


def getxml(urls):
    r = requests.get(urls)
    return r.content


def prasezhishus(strings):
    root = ET.fromstring(strings)
    zhishus = root.find('zhishus')
    for zhishu in zhishus.findall('zhishu'):
        name = zhishu.find('name').text.encode('utf-8')
        value = zhishu.find('value').text.encode('utf-8')
        detail = zhishu.find('detail').text.encode('utf-8')
        yield (name, value, detail)


def getcputemperature():
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


def main():
    url = "http://wthrcdn.etouch.cn/WeatherApi?citykey=101060903"

    muxml = getxml(url)
    print("get url")
    for name, value, detail in prasezhishus(muxml):
        if name == "穿衣指数":
            print('穿衣指数：{}, 小贴士：{}'.format(value, detail))

    cputemp = getcputemperature()
    print(cputemp)
    pass


if __name__ == '__main__':
    main()
