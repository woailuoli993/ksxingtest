#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
一个需要计算的入群申请:
求
1<=i<=10**12 范围内所有d(i)的和的末尾的12位
其中d(i) 表示i的正约数的和 i 位整数
群号
"""
import time

def d(n):
    '''
    求i的正约数的和
    :return 1到n  的约数和的和
    '''

    mysum = 0
    mid = int(n**0.5) + 1
    for i in range(1, mid):
        mysum += n/i*i + (n/i + mid) * (n/i - mid + 1)/2
    return mysum



def dothers(n):
    s = 0
    for i in range(1, int(n**0.5)+1):
        s += n/i*i

    i = int(n**0.5)+1
    for j in range(n/i, 0, -1):
        s += j * ((i+n/j)*(n/j-i+1)/2)
        i = n/j+1

    return s



"""
知乎上找到了想要的解决方案:
关于连续数的约数规律:
每一个数都有约数1
每两个数才有一个约数2
没三个数才有一个约数3
....以此类推
设n为总数
1的个数为n/1*n
2的个数为n/2
最后相加  此方法的复杂度为o(0)

另一种  需作图可得出规律
例如 求1-10 的约数和
可先求出 sqrt(10)
10 / 1到sqrt(10)  得到所有整数
做多个步长为1的等差数列求和
本宝宝用的是混合法.
"""

if __name__=='__main__':
    start = time.time()
    mm = d(10**12)
    print(mm)
    print('cost time:{}'.format(time.time()-start))
    mmstr = str(mm)
    print mmstr[-12:]
