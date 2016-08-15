import requests
from config import WECHAT_OFICAL_APPID, WECHAT_OFICAL_SCERCT
from wechatpy import WeChatClient

def getWeChatToken():
    client = WeChatClient(WECHAT_OFICAL_APPID, WECHAT_OFICAL_SCERCT)
    info = client.fetch_access_token()
    print(info)


if __name__=='__main__':
    getWeChatToken()
