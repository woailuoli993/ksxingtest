# -*- coding: utf-8 -*-

import requests
from urllib.parse import quote
from lxml import etree

_HOST = 'https://www.baidu.com'
_HEADER = {
    'Host': 'www.baidu.com',
    'Referer': 'https://www.baidu.com/',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/73.0.3683.86 Safari/537.36',
    'Cookie': 'BAIDUID=6CFAF38B4301A72B07E07AE6287918EE:FG=1;'
              ' BIDUPSID=6CFAF38B4301A72B07E07AE6287918EE; '
              'PSTM=1555657733; '
              'BD_UPN=12314753; '
              'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'H_PS_PSSID=1452_21115_29063_28519_29099_28839_28584_26350_'
              '22160; '
              'BDSFRCVID=OQLOJeC62ZbEQf79NmZQrgem622j9VoTH6aopgl0g7g6LxhLr'
              'VdQEG0Pjx8g0Kub1VDqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0P3J; '
              'H_BDCLCKID_SF=tJIJ_K02tCL3fP36qRJHh40e5frjetJyaR39blRvWJ5TM'
              'CoL-xoGb6b-XxczQRjM5CDqoDo_fxQoShPC-tn2bP7QbNJMtf7O2gJH-Jbl'
              '3l02Vbc9e-t2ynLVDJjRb4RMW20e0h7mWIbmsxA45J7cM4IseboJLfT-0bc'
              '4KKJxthF0HPonHj_ae5O03f; '
              'delPer=0; '
              'BD_CK_SAM=1; '
              'PSINO=7; BD_HOME=0; '
              'COOKIE_SESSION=1077_0_9_9_2_10_0_3_9_6_1_0_0_0_3_0_15591151'
              '43_0_1559116217%7C9%2383853_11_1559110087%7C3; '
              'H_PS_645EC=57b5CqZRjp1CCadAxqifmhJbKYEzUtcCzO7zQX7y9vg0fsSp'
              'QV7PT7xvEAg'
}


def get_url(wd, idx):
    temp_url = _HOST + '/s?wd={}&pn={}'
    return temp_url.format(quote(wd), str((idx - 1) * 10))


def get_content(url):
    """
    :return: xml object, response
    """
    res = requests.get(url, headers=_HEADER)
    return etree.HTML(res.text), res


def _parse_block(block):
    b_url = block.find('.//h3/a').get('href')
    b_title = ''.join(block.find('.//h3').itertext())
    b_desc = ''.join(block.find('.//*[@class="c-abstract"]').itertext())
    b_date = b_desc.split('\xa0')[0] if len(b_desc.split('\xa0')) > 0 else None
    return b_url, b_title, b_date, b_desc


def page_query(content):
    """
    current page blocks info list.
    :param content: xml obj
    :return: list
    """
    # info blocks
    blocks = content.xpath('//*[@class="result c-container "]')
    return list(map(_parse_block, blocks))


def get_next_page(content):
    return _HOST + content.findall('.//*[@class="n"]')[-1].get('href')


def query(wd, pages):
    url = get_url(wd, 1)  # init with page=0
    data_set = []
    print('[+]..start')
    for p in range(pages):
        content, _ = get_content(url)
        page_set = page_query(content)
        data_set.extend(page_set)
        next_url = get_next_page(content)
        if next_url:
            print('[+] >> {} done.'.format(p+1))
            url, next_url = next_url, None
        else:
            print("没了。。。")
            break
    return data_set


if __name__ == '__main__':
    data = query("棋牌政策", 10)
    print(data)
