# -*- coding: utf-8 -*-
"""
用于测试 联通 - cisco jasper restful api
"""
import requests

import datetime
import pytz
from requests.auth import HTTPBasicAuth
base_url = 'https://api.10646.cn/rws/api/'
version = 'v1'

API_DEVICES = '/devices'

TZ = pytz.timezone('Asia/Shanghai')


def query_device(account_id, account_name, api_token, modified_since,
                 status=None,
                 page_size=50,
                 page_number=1):
    url = ''.join((base_url, version, API_DEVICES))
    params = dict(accountID=account_id,
                  modifiedSince=modified_since,
                  pageSize=page_size,
                  pageNumber=page_number)
    auth = HTTPBasicAuth(account_name, api_token)
    print(auth)
    if status is not None:
        params['status'] = status

    rq = requests.get(url, params=params, auth=auth)
    print(rq.url)
    print(rq.content)
    return rq.status_code


if __name__ == '__main__':
    print(query_device(account_id=raw_input('account_id:'),
                       account_name=raw_input('name:'),
                       api_token=raw_input('token:'),
                       modified_since=
                       datetime.datetime(2017, 1, 1, tzinfo=TZ).isoformat()))
