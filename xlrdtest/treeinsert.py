# _*_ coding:utf-8 _*_

"""
需求说明 :
在试题类型表中类别为一个典型的树结构
mysql 表结构 :      id: 节点id
                    name: 节点名
                    company_id: 公司id
                    pid: 父节点id(root id == 0)
给定一个由 /分割的字符串  然后按要求添加节点
eg : "测试/金融"  处理后 会在 树上添加 : 根-> 测试 -> 金融
"""

# 处理分类字符串并添加到class,并返回目标节点id
def formatToClassTree(classstr):

    classstr = classstr.strip()
    # 查询父节点id
    # rootid =
    if classstr=="":
        return rootid
    else:
        clist = classstr.split('/')

        clist.insert(0, rootid)   # 添加父节点id 到 list头 使用deque可以提高效率
        return reduce(addnodeToClassTree, clist)


def addnodeToClassTree(pid, cname):
    """使用reduce 添加试题分类"""
    pass



"""
[{'status': 'enable',
  'key8': '0',
  'create_date': datetime.datetime(2016, 9, 6, 11, 54, 53, 690985),
  'classification': u'1',
  'key3': '0',
  'answer4': '9.15\r',
  'key1': '0',
  'answer1': '12\r',
  'key6': '0',
  'answer3': '23\r',
  'answer2': '22 \r',
  'key5': '0',
  'encrypt': '0',
  'key7': '0',
  'key4': '1',
  'cop_id': 1L,
  'question': '\xe8\xa1\xac\xe8\xa1\xa3\xe7\x9a\x84\xe4\xbb\xb7\xe6\xa0\xbc\xef\xbc\x9f\r',
  'analysis': '\xe6\x98\x93\xe5\xbe\x97\r',
  'creater': u'heyuhua@ksxing.com',
  'key2': '0',
  'tab_num': 4,
  'type': u'1',
  'difficult': u'simple'}]

{'status': 'enable',
 'cop_id': 1L,
 'uploadwey': 'excel',
 'answer1': u'\u4f7f\u7528\u5176\u4ed6\u8f66\u8f86\u884c\u9a76\u8bc1',
 'key1': 1,
 'question': u'\u9a7e\u9a76\u4eba\u6709\u4e0b\u5217\u54ea\u79cd\u8fdd\u6cd5\u884c\u4e3a\u4e00\u6b21\u8bb01\u5206\uff1f',
 'analysis': u'\u8bf7\u4ed4\u7ec6\u9605\u8bfb\u4ea4\u89c4',
 'answer2': u'\u996e\u9152\u540e\u9a7e\u9a76\u673a\u52a8\u8f66',
 'creater': u'heyuhua@ksxing.com',
 'answer3': u'\u8f66\u901f\u8d85\u8fc7\u89c4\u5b9a\u65f6\u901f50%\u4ee5\u4e0a',
 'tab_num': 1,
 'answer4': u'\u8fdd\u6cd5\u5360\u7528\u5e94\u6025\u8f66\u9053\u884c\u9a76',
 'create_date': datetime.datetime(2016, 9, 6, 17, 47, 20, 405198),
 'type': u'1',
 'classsification': '1',
 'difficult': 'simple'}

{'status': 'enable',
 'key8': 1,
 'cop_id': 1L,
 'uploadwey': 'excel',
 'answer5': u'\u8fdd\u6cd5\u5360\u7528\u5e94\u6025\u8f66\u9053\u884c\u9a76',
 'answer1': u'\u4f7f\u7528\u5176\u4ed6\u8f66\u8f86\u884c\u9a76\u8bc1',
 'answer7': u'\u8fdd\u6cd5\u5360\u7528\u5e94\u6025\u8f66\u9053\u884c\u9a76',
 'answer6': u'\u8fdd\u6cd5\u5360\u7528\u5e94\u6025\u8f66\u9053\u884c\u9a76',
 'question': u'\u9a7e\u9a76\u4eba\u6709\u4e0b\u5217\u54ea\u79cd\u8fdd\u6cd5\u884c\u4e3a\u4e00\u6b21\u8bb099\u5206\uff1f',
 'analysis': u'\u8bf7\u4ed4\u7ec6\u9605\u8bfb\u4ea4\u89c4',
 'answer2': u'\u996e\u9152\u540e\u9a7e\u9a76\u673a\u52a8\u8f66',
 'creater': u'heyuhua@ksxing.com',
 'answer3': u'\u8f66\u901f\u8d85\u8fc7\u89c4\u5b9a\u65f6\u901f50%\u4ee5\u4e0a',
 'tab_num': 1,
 'answer4': u'\u8fdd\u6cd5\u5360\u7528\u5e94\u6025\u8f66\u9053\u884c\u9a76',
 'create_date': datetime.datetime(2016, 9, 6, 17, 47, 20, 405198),
 'difficult': 'middle',
 'type': u'1',
 'classsification': 23837L,
 'answer8': u'\u968f\u610f\u98d9\u8f66'}


ids:
57ce944d97b2316edeedcadd
57ce944d97b2316edeedcade
57ce944d97b2316edeedcadf

57ce973497b23170a4593a1d
57ce973497b23170a4593a1e
57ce973497b23170a4593a1f

57ce98f197b23171cbd44b78
57ce98f197b23171cbd44b79
57ce98f197b23171cbd44b7a

57ce9ad597b23172b6b665c1
57ce9ad597b23172b6b665c2
57ce9ad597b23172b6b665c3
"""
