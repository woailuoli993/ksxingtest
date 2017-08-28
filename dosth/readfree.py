# -*- coding: utf-8 -*-
import requests
import logging

from .config import READFREE_COOKIE

url = 'http://readfree.me/accounts/checkin'
cookie_str = ''  # 需要登录到readfree上获取当时的cookie值，然后直接使用该cookie值进行登录签到

logging.basicConfig(
    level=logging.INFO,
    filename='./readfree_auto_sig.log',
    filemode='a',
    format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')

if __name__ == "__main__":

    cookies = READFREE_COOKIE
    for ck in cookie_str.split(';'):
        name, value = ck.strip().split('=', 1)
        cookies[name] = value

    logging.info('start to sign ...')
    ret = requests.get(url, cookies=cookies)
    logging.info('sign %s' % ret)

