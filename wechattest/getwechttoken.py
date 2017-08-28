from dosth.config import WECHAT_OFICAL_APPID, WECHAT_OFICAL_SCERCT
from wechatpy import WeChatClient
from wechatpy import WeChatClient

from dosth.config import WECHAT_OFICAL_APPID, WECHAT_OFICAL_SCERCT


def getWeChatToken():
    client = WeChatClient(WECHAT_OFICAL_APPID, WECHAT_OFICAL_SCERCT)
    info = client.fetch_access_token()
    print(info)


if __name__=='__main__':
    getWeChatToken()
