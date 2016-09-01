# _*_  coding: utf-8 _*_


def addOneSum(a):
    '''
    赶时髦可以用mapreduce
    '''
    a_str = str(a)

    mysum = 0
    for i in a_str:
        i_int = int(i)
        mysum += i_int

    return mysum


def getRes(a):

    temp = addOneSum(a)
    while temp > 10:
        temp = addOneSum(temp)

    return temp

if __name__=="__main__":

    print(getRes(38))
