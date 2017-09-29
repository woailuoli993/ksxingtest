#_*_coding:utf-8_*_

# cl = SphinxClient()
# cl.SetServer('localhost', 9312)     #创建链接
# cl.SetWeights([100,1])              #
# cl.SetMatchMode(SPH_MATCH_ANY)
# cl.SetSelect("*, ln(o_id) AS obid")
# print '[!]Status:'
# print '[!]err:------', cl.GetLastError()
# print '[+]res!----------'
# res = cl.Query('中央')
# print res
# print '[!]err:------', cl.GetLastError()
# print cl.__doc__
# print cl.__dict__
# print cl.Status()
a = {'b': 1 if 1+1==1 else 2,
     'xixi': 'dada'}
print a

if 'b' in a.keys():
    print '1'